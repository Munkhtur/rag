import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "mongol.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongoltxt_110")

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # Read the text content from the file
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Create embeddings
    print("\n--- Creating embeddings ---")
#     embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# )
    
#     embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-mpnet-base-v2"
# )
    embeddings = HuggingFaceEmbeddings(
    model_name="gmunkhtur/finetuned_paraphrase-multilingual"
)
    # embeddings = GoogleGenerativeAIEmbeddings(model="models/text-multilingual-embedding-002")

    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it automatically
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating vector store ---")

else:
    print("Vector store already exists. No need to initialize.")