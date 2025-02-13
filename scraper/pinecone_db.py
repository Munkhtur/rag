import glob
from io import StringIO
import json
import os
import traceback
from pinecone import Pinecone, ServerlessSpec
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import tqdm
from langchain_core.documents import Document   
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import time
from langchain_pinecone import PineconeVectorStore

load_dotenv(override=True)

pc = Pinecone()


index_name = "tdb"  # change if desired

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
file_path = os.path.join(current_dir, "books", "part_1.txt")
# persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongol_test")

embeddings = HuggingFaceEmbeddings(
        model_name="gmunkhtur/finetuned_paraphrase-multilingual_test"
    )


vector_store = PineconeVectorStore(index=index, embedding=embeddings)
data_path = "./data/*/final_data.json"
docs = []
# Loop through each final_data.json file
for i, file_path in enumerate( glob.glob(data_path)):
    print(file_path)
    if i == 0:

    # topic = os.path.basename(os.path.dirname(file_path))  # Extract topic name from path
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)  # Store data with topic as the key
            for d in data:
                doc = Document( page_content=d.get("chunk", ""),metadata={"source": d.get("source", "")})
                docs.append(doc)
vector_store.add_documents(docs)