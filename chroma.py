import chromadb
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings(
model_name="gmunkhtur/paraphrase-mongolian-minilm-mntoken"
)
vector_store = Chroma(

    persist_directory="./db/chroma_db_mongoltxt_token",  # Where to save data locally, remove if not necessary
)


# Get the collection
# persistent_client = vector_store.get()
# collection = vector_store.get()
# Retrieve all documents
results = vector_store.get(include=["documents", "metadatas"])
# print("Result",results)
# Print all the data
with open("results2.txt", "w", encoding="utf-8") as file:
    # Loop through each document and write it to the file
    for result in results['documents']:
        file.write(result + "\n\n") 
        file.write( "------------------------------------------------\n\n") 


for document, metadata in zip(results['documents'], results['metadatas']):
    print(f"Document: {document}")
    print(f"Metadata: {metadata}")



