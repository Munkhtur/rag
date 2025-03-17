import os

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import time
from langchain_cohere import CohereRerank

load_dotenv(override=True)

pc = Pinecone()


index_name = "tdb-v2"  # change if desired

existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)


# persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongol_test")

embeddings = HuggingFaceEmbeddings(
        model_name="gmunkhtur/finetuned_tdb_paraphrase-multilingual_mpnet_try6"
    )
# embeddings.embed_query()


vector_store = PineconeVectorStore(index=index, embedding=embeddings)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("gmunkhtur/finetuned_tdb_paraphrase-multilingual_mpnet_try6")

text = "Та ямар зээлийн үйлчилгээтэй вэ?"

vector = model.encode(text).tolist()
import json
with open("vector.json", "w", encoding="utf-8") as f:
    json.dump(vector, f, ensure_ascii=False)

# print(embeddings.embed_query("Зээл\n\n## Хэрэглээний зээл\n\n* Цалингийн зээл\n* Хэрэглээний цахим зээл\n* Хялбар зээ"))
# print(embeddings.embed_documents(["Зээл\n\n## Хэрэглээний зээл\n\n* Цалингийн зээл\n* Хэрэглээний цахим зээл\n* Хялбар зээ"]))

# Define the user's question
query = "Та ямар зээлийн үйлчилгээтэй вэ?"



# Retrieve relevant documents based on the query
# retriever = vector_store.as_retriever(
#     search_type="similarity_score_threshold",
#     search_kwargs={"k": 3, "score_threshold": 0.5},
# )

# retriever = db.as_retriever(
#     search_type="mmr",
#     search_kwargs={"k": 10, "fetch_k": 20, "lambda_mult":0.1},
# )
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":10},
)
relevant_docs = retriever.invoke(query)

# Display the relevant results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")