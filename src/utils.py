import bs4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings

template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Be helpful in your answer and be sure to reference the following context when possible.

{context}

Question: {question}

Answer:"""
prompt = PromptTemplate.from_template(template)

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)

def _load_documents(url:str):
    loader = WebBaseLoader(
        web_paths=(url,), # "https://lilianweng.github.io/posts/2023-06-23-agent/"
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    docs = loader.load()
    return docs

def _split_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return splits

def _get_embedding_retriever(splits):
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_function)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    return retriever

def _format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def _get_chain(retriever, prompt, llm):
    rag_chain = (
        {"context": retriever | _format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

def url_qa(url: str, question: str):
    docs = _load_documents(url)
    splits = _split_documents(docs)
    retriever = _get_embedding_retriever(splits)
    rag_chain = _get_chain(retriever, prompt, llm)
    response = rag_chain.invoke(question)
    return response


