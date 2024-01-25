"""
Utility functions used in the RAG app.
"""

import base64
from typing import List

from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.runnables.base import Runnable
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

TEMPLATE = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Be helpful in your answer and be sure to reference the following context when possible.

{context}

Question: {question}

Answer:"""

prompt = PromptTemplate.from_template(TEMPLATE)
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)


def _save_doc_locally(pdf_string: str, path: str = "./document.pdf") -> str:
    """
    Decodes the base64 string representation of the pdf document
    and saves it to a local path.

    Args:
        pdf_string (str): Base64 string representation of the pdf document.
        path (str): Local path to save pdf document to.

    Returns:
        str: Local path where pdf document was saved to.
    """
    # Decode the base64 string to bytes
    decoded_bytes = base64.b64decode(pdf_string)
    if decoded_bytes[0:4] != b"%PDF":
        raise TypeError("Invalid PDF file received.")

    # Save pdf file
    with open(path, "wb") as _f:
        _f.write(decoded_bytes)

    return path


def _load_and_split_doc(pdf_path: str) -> List[Document]:
    """
    Loads the content of the pdf document and separates it
    into chunks for embedding.

    Args:
        pdf_path (str): Local path to pdf document.

    Returns:
        List[Document]: Document chunks (splits).
    """
    loader = PyPDFLoader(pdf_path)
    splits = loader.load_and_split(
        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, add_start_index=True
        )
    )
    return splits


def _get_embedding_retriever(splits: List[Document]) -> VectorStoreRetriever:
    """
    Embeds all the document chunks/splits and returns the
    appropriate similarity retriever for the vector database used.

    Args:
        splits (List[Document]): Document chunks/splits.

    Returns:
        VectorStoreRetriever: Vector store retriever.
    """
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_function)
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 5}
    )
    return retriever


def _format_docs(docs: List[str]) -> str:
    """
    Join all documents into single string, separated
    by double newline characters.
    """
    return "\n\n".join(doc.page_content for doc in docs)


def _get_chain(
    retriever: VectorStoreRetriever, prompt: PromptTemplate, llm: BaseChatModel
) -> Runnable:
    """
    Creates a RAG chain using LCEL (LangChain Expression Language).

    Args:
        retriever (VectorStoreRetriever): A vector store retriever.
        prompt (PromptTemplate): The prompt template that includes the content
            retrieved from the vector store and the question.
        llm (BaseChatModel): The LLM that will be used to answer the question.

    Returns:
        Runnable: A Runnable object that represents the RAG chain.
    """
    rag_chain = (
        {"context": retriever | _format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain


def get_answer(pdf_string: str, question: str) -> str:
    """
    Run the RAG cycle and return the answer to the question.

    Args:
        pdf_string (str): The base64 encoded string representation of the PDF document.
        question (str): The question you want to ask about the PDF document.

    Returns:
        str: The answer to the given question.
    """
    pdf_path = _save_doc_locally(pdf_string, path="./document.pdf")
    splits = _load_and_split_doc(pdf_path)
    retriever = _get_embedding_retriever(splits)
    rag_chain = _get_chain(retriever, prompt, llm)
    response = rag_chain.invoke(question)
    return response
