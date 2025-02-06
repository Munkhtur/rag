
from elasticsearch import Elasticsearch
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
from langchain_core.messages import HumanMessage, SystemMessage



load_dotenv(override=True)
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


current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongoltxt_110")

embeddings = HuggingFaceEmbeddings(model_name="gmunkhtur/finetuned_paraphrase-multilingual_test")
# db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)
db = PineconeVectorStore(index=index, embedding=embeddings)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 10})



index_name_es = "documents"


es = Elasticsearch('http://localhost:9200')

query =  "Х. Чойбалсан ямар сургуульд багшилж байсан бэ?"

es_query = {
    "query": {
        "match": {
            "content": query
        }
    }
}

response = es.search(index=index_name_es, body=es_query)



bm25_docs = [
    Document(
        page_content=row['_source']['content'],
        id = row["_id"],  # Content
        metadata={ "score": row["_score"], "source": "es"}
    )
    for row in response["hits"]["hits"]
]


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


combined_results = bm25_docs + vector_results 


cohere_reranker = CohereRerank(model="rerank-multilingual-v2.0", top_n=5)
reranked_results = cohere_reranker.compress_documents(combined_results, query)
# reranked_results = cohere_reranker.rerank(combined_results, query, top_n=5)




for doc in reranked_results:
    print(f"Source: {doc.metadata["source"]} \nContent: {doc.page_content}\n")
    # print(f" \nContent: {doc.page_content}\n")

print("vec", len(vector_results))
print("text", len(bm25_docs))
for doc in bm25_docs:
    print(f"elastic Source: {doc.metadata["source"]} \nContent: {doc.page_content}\n")
print("rerank", len(reranked_results))


combined_input = (
    "Here are some documents that might help answer the question: "
    + query
    + "\n\nRelevant Documents:\n"
    + "\n\n".join([doc.page_content for doc in reranked_results])
    + "\n\nPlease provide an answer based only on the provided documents. Respond only in Mongolian. If the answer is not found in the documents, respond with 'I'm not sure'."
)

print("loading chat model")
# Create a ChatOpenAI model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

print("loaded chat model")
# Define the messages for the model
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=combined_input),
]

print("invoking")
# Invoke the model with the combined input
result = model.invoke(messages)

# Display the full result and content only
print("\n--- Generated Response ---")
# print("Full result:")
# print(result)
print("Content only:")
print(result.content)