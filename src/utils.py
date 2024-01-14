import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

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
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()
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


