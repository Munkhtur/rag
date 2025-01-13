import chromadb
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "all_articles.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongol_test")

embedding_function = HuggingFaceEmbeddings(
    model_name="gmunkhtur/finetuned_paraphrase-multilingual"
)
langchain_chroma = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_function,
)


# Get the collection
# persistent_client = vector_store.get()
# collection = vector_store.get()
# Retrieve all documents
# results = langchain_chroma.get(include=["documents", "metadatas"])
# print("Result",results)
# Print all the data
# Print the last 5 documents and their corresponding metadata
print("There are", langchain_chroma._collection.count(), "in the collection")
