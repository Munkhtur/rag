import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
from langchain_community.retrievers import BM25Retriever


# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "mongol.txt")
# persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongoltxt_110")


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
bm25_retriever = BM25Retriever.from_documents(docs)
bm25_retriever.persist("./bm25_retriever")