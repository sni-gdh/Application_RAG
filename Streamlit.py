import streamlit as st
import time

from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import  ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings

local_llm = ChatOllama(model="mistral")

def rag(collection_name):
    vectorstore = Chroma(
        collection_name = collection_name,
        embedding_function =  OllamaEmbeddings(model="nomic-embed-text"),
        persist_directory="./chroma_db"
    )

    retriever = vectorstore.as_retriever()

    prompt_template = """Answer the question based on the following context:
    {context}
    Question : {question}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    chain = (
        {"context" : retriever , "question" : RunnablePassthrough() }
        | prompt
        |local_llm
        | StrOutputParser()
        )
    return chain, retriever

chain, retriever = rag("recursive-chunks")

st.title("RAG Question Answering")

question = st.text_input("Enter your question")

if question:

    start_time = time.time()

    # generate answer
    answer = chain.invoke(question)

    end_time = time.time()

    response_time = end_time - start_time

    # Answer
    st.subheader("Answer")
    st.write(answer)

    # Response time
    st.subheader("Query Time")
    st.write(f"{response_time:.2f} seconds")