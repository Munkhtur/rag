from langchain_pinecone import PineconeVectorStore

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks.manager import CallbackManagerForRetrieverRun
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain.prompts import ChatPromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain_core.vectorstores import VectorStoreRetriever
from elasticsearch import Elasticsearch
import os
import time
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain.schema import Document
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from langchain_core.messages import HumanMessage,AIMessage
from langchain_cohere import CohereRerank

app = FastAPI()

load_dotenv(override=True)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Pinecone Setup
pc = Pinecone()
index_name = "tdb-v2"

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

# Elasticsearch Setup (Keyword Search Only)
es = Elasticsearch("http://localhost:9200")
index_name_es = "tdb"

# Initialize embeddings for Pinecone only
embeddings = HuggingFaceEmbeddings(model_name="gmunkhtur/finetuned_tdb_paraphrase-multilingual_mpnet_try6")

# Pinecone Vector Store
db_pinecone = PineconeVectorStore(index=index, embedding=embeddings)
pinecone_retriever = db_pinecone.as_retriever(search_type="similarity", search_kwargs={"k": 10})


# print("pine",pinecone_retriever.invoke("Х. Чойбалсан хэдэн насандаа Санбэйсийн хүрээнд шавилан сууж сахил хүртсэн бэ?"))
# Elasticsearch Keyword Search Retriever
class ElasticsearchKeywordRetriever(BaseRetriever):
    es_client: Elasticsearch  # Define explicitly
    index_name: str  # Define explicitly
    def __init__(self, es_client: Elasticsearch, index_name: str, **kwargs):
        super().__init__(es_client=es_client, index_name=index_name, **kwargs)
        self.es_client = es_client
        self.index_name = index_name

    def _get_relevant_documents(self, query:str, *, run_manager: CallbackManagerForRetrieverRun ):
        print("es query", query)
        es_query = {
            "query": {
                "match": {
                    "content": query  # Simple keyword match
                }
            },
            "size": 10  # Return top 3 matches
        }
        response = self.es_client.search(index=self.index_name, body=es_query)
        res = [
                Document(page_content=hit["_source"]["content"] + "\nelastic search\n",metadata=hit["_source"]) 
                for hit in response["hits"]["hits"]
            ]
            

    
        return res

es_retriever = ElasticsearchKeywordRetriever(es, index_name_es)

# Combined Retriever: Merge Pinecone & Elasticsearch Results
class CombinedRetriever(BaseRetriever):
    pinecone_retriever: VectorStoreRetriever
    es_retriever: ElasticsearchKeywordRetriever
    # def __init__(self, pinecone_retriever: VectorStoreRetriever, es_retriever: ElasticsearchKeywordRetriever, **kwargs):
    #     super().__init__(**kwargs)
    #     self.pinecone_retriever = pinecone_retriever
    #     self.es_retriever = es_retriever

    def _get_relevant_documents(self, query,*, run_manager: CallbackManagerForRetrieverRun):
        pinecone_results = self.pinecone_retriever.invoke(query)
        es_results = self.es_retriever.invoke(query)

        # Initialize both models
        cohere_default = CohereRerank(model="rerank-multilingual-v3.0", top_n=5)
        # Retrieve results
        combined_results = pinecone_results + es_results

        # Rerank with both models
        reranked_default = cohere_default.compress_documents(combined_results, query)
        print("RERANKEd")
        for r in reranked_default:
            print(r)
            print("+++++++++++++++++++++++++++")
        print("pinecome")
        for r in pinecone_results:
            print(r)
            print("+++++++++++++++++++++++++++")
        return reranked_default  # Combine results
    # def model_dump(self, exclude_defaults=True, exclude_none=True):
    #     return super().model_dump(exclude_defaults=exclude_defaults, exclude_none=exclude_none)
retriever = CombinedRetriever(pinecone_retriever=pinecone_retriever, es_retriever=es_retriever)
retriever_data = retriever.model_dump(exclude_defaults=True, exclude_none=True)
# Contextualization Prompt
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

history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

# QA Prompt
qa_system_prompt = (
    "You are a virtual assistant for  Худалдаа Хөгжлийн Банк, designed to help customers "
    "with banking-related inquiries only. Use the retrieved information below to provide "
    "accurate and concise answers with suggestions in Mongolian. If the answer is not found in the provided context, "
    "or if the question is unrelated to the bank "
    "politely inform the user that you don’t have the information and suggest alternative actions or"
    "inform the user that you can only answer banking-related questions."
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

# Final Chain
question_answer_chain = create_stuff_documents_chain(ChatGoogleGenerativeAI(model="gemini-2.0-flash"), qa_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
chat_histories = {}
# query =  "Х. Чойбалсан хэдэн насандаа Санбэйсийн хүрээнд шавилан сууж сахил хүртсэн бэ?"
# result = rag_chain.invoke({"input": query, "chat_history": chat_history})


# print("resil;t", result)
class QueryRequest(BaseModel):
    user_id: str
    query: str


@app.post("/query")
async def get_response(request: QueryRequest):
    user_id = request.user_id

    if user_id not in chat_histories:
        chat_histories[user_id] = []
    chat_history = chat_histories[user_id]

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

