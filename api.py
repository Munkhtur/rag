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
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, just "
    "reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

qa_system_prompt = (
    "You are an assistant for question-answering tasks. Use "
    "the following pieces of retrieved context to answer the "
    "question. If you don't know the answer, just say that you "
    "don't know. Use three sentences maximum and keep the answer "
    "concise."
    "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
chat_histories: Dict[str, List] = {}
# Define request and endpoint
class QueryRequest(BaseModel):
    user_id: str
    query: str

@app.post("/query")
async def get_response(request: QueryRequest):
    user_id = request.user_id

    if user_id not in chat_histories:
        chat_histories[user_id] = []
    chat_history = chat_histories[user_id]

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    relevant_docs = retriever.invoke(request.query)
    combined_input = (
    "Here are some documents that might help answer the question: "
    + request.query
    + "\n\nRelevant Documents:\n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    + "\n\nPlease provide an answer based only on the provided documents. Respond only in Mongolian. If the answer is not found in the documents, respond with 'I'm not sure'."
)
    messages = [HumanMessage(content=combined_input)]
    result = llm.invoke(messages)
    return {
        "query": request.query,
        "relevant_documents": [doc.page_content for doc in relevant_docs],
        "response": result.content
    }

@app.post("/chat")
async def continual_chat(request: QueryRequest):

    user_id = request.user_id

    if user_id not in chat_histories:
        chat_histories[user_id] = []
    chat_history = chat_histories[user_id]
    print(chat_history)
    result = rag_chain.invoke({"input": request.query, "chat_history": chat_history})
    chat_history.append(HumanMessage(content=request.query))
    chat_history.append(AIMessage(content=result["answer"]))
    return {
        "query": request.query,
        "response": result["answer"]
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

