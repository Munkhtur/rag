import os
import time
from typing import Dict, List
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage,AIMessage
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from uuid import uuid4
from jwt import decode, exceptions, encode
import psycopg2
from langchain.schema import Document
from langchain_cohere import CohereRerank



# Load environment variables
load_dotenv(override=True)

app = FastAPI()

pc = Pinecone()

index_name = "langchain-mongol-context"  # change if desired

existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)

# Initialize embeddings and vector store
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongoltxt_110")

embeddings = HuggingFaceEmbeddings(model_name="gmunkhtur/finetuned_paraphrase-multilingual_test")
# db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)
db = PineconeVectorStore(index=index, embedding=embeddings)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 10})






conn = psycopg2.connect(
    dbname="postgres",
    user="postgres", 
    password="123456", 
    host="localhost", 
    port="5432"
)


cur = conn.cursor()

cur.execute('SET search_path TO textsearch;')

query_search = """
    SELECT id, content , ts_rank(ts_vector, plainto_tsquery('simple', %s)) AS rank
    FROM documents
    WHERE ts_vector @@ plainto_tsquery('simple', %s)
    ORDER BY ts_rank(ts_vector, plainto_tsquery('simple', %s)) DESC LIMIT 5;
"""
query =  "Сайншанд аль аймгийн сум бэ?"

vector_results = retriever.invoke(query)

vector_results = [
    Document(
        page_content=match.page_content,  # Store actual text
        metadata={
          # Pinecone similarity score
            "source": "Pinecone",      # Manually add "Pinecone" as source        # Optionally store document ID
        }
    )
    for match in vector_results
]
cur.execute(query_search, (query, query,query))


keyword_results = cur.fetchall()


# print(keyword_results)
# for vec in vector_results:
#     print(vec, "\n")

# combined_results = []

bm25_docs = [
    Document(
        page_content=row[1],
        id = row[0],  # Content
        metadata={ "score": row[2], "source": "BM25"}
    )
    for row in keyword_results
]

combined_results = bm25_docs + vector_results 


cohere_reranker = CohereRerank(model="rerank-multilingual-v2.0")

reranked_results = cohere_reranker.compress_documents(combined_results, query)


for doc in reranked_results:
    print(f"Source: {doc.metadata["source"]} \nContent: {doc.page_content}\n")

print("vec", len(vector_results))
print("text", len(bm25_docs))