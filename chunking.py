from rich import print
from langchain_core.documents import Document
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import  ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings
from typing import List
from pydantic import BaseModel
from langchain_classic import hub
from dotenv import load_dotenv
import json
import os
from agentic_chunker import AgenticChunker
from langchain_openai import ChatOpenAI
import re


local_llm = ChatOllama(model="mistral")

#RAG
def rag(chunks ,collection_name):
    vectorstore = Chroma.from_documents(
        documents = chunks,
        collection_name = collection_name,
        embedding =  OllamaEmbeddings(model="nomic-embed-text"),
        persist_directory="./chroma_db"
    )
    retiever = vectorstore.as_retriever()
    prompt_template = """Answer the question based on the following context:
    {context}
    Question : {question}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    chain = (
        {"context" : retiever , "question" : RunnablePassthrough() }
        | prompt
        |local_llm
        | StrOutputParser()
        )
    result = chain.invoke("What is the capital of France?")
    print(result)

import fitz  # pymupdf
text = ""

with fitz.open("file_pdf1.pdf") as doc:
    for page in doc:
        text += page.get_text() + "\n"

with fitz.open("file_pdf2.pdf") as doc:
    for page in doc:
        text += page.get_text() + "\n"

paragraphs = re.split(r"\n\s*\n", text)

#recursive character text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
documents = text_splitter.create_documents([text])
rag(documents, "recursive-chunks")


# #agentic chunking
# load_dotenv()
# prompt_template = hub.pull("wfh/proposal-indexing")

# llm = ChatOpenAI(
#     model="Qwen/Qwen3.5-35B-A3B:novita",
#     api_key=os.getenv("MY_HUGGINGFACE_API"),
#     base_url="https://router.huggingface.co/v1"
# )

# runnable  = prompt_template | llm

# class Sentences(BaseModel):
#     sentences: List[str]

# extraction_chain = llm.with_structured_output(Sentences)
# def get_propositions(text):
#     runnable_output = runnable.invoke({
#         "input" : text
#     }).content
    
#     propositions = extraction_chain.invoke(runnable_output).sentences
#     return propositions

# text_propositions = []

# for i, para in enumerate(paragraphs[:5]):
#     propositions = get_propositions(para)
#     text_propositions.append(propositions)
#     print(f"Done with {i}")
# print(f"You have {len(text_propositions)} propositions")
# # print(text_propositions[:10])

# # Group Chunk
# ac = AgenticChunker(os.getenv("MY_HUGGINGFACE_API"), "meta-llama/Llama-3.1-8B-Instruct:novita", "https://router.huggingface.co/v1")
# ac.add_propositions(text_propositions)
# print(ac.preety_print_chunks())
# chunks = ac.get_chunks(get_type = 'list of strings')
# print(chunks)
# documents = [Document(page_content = chunk, metadata = {'source' : "local"}) for chunk in chunks]
# rag(documents, "agentic-chunks")