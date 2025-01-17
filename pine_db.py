from io import StringIO
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
file_path = os.path.join(current_dir, "books", "part_1.txt")
# persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongol_test")

embeddings = HuggingFaceEmbeddings(
        model_name="gmunkhtur/finetuned_paraphrase-multilingual_test"
    )


vector_store = PineconeVectorStore(index=index, embedding=embeddings)



# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# with open(file_path, "r", encoding="utf-8") as file:
#     content = file.read()

# # # Split the content into paragraphs (assuming paragraphs are separated by new lines)
# paragraphs = content.split("\n\n")
# first_paragraph = paragraphs[13]

# db = Chroma(
#     persist_directory=persistent_directory,
#     embedding_function=HuggingFaceEmbeddings(
#         model_name="gmunkhtur/finetuned_paraphrase-multilingual"
#     ),
# )

# for paragraph in paragraphs:

#     try:
#         document = [Document(page_content=paragraph)]

#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=1000, chunk_overlap=100
#         )
#         docs = text_splitter.split_documents(document)

#         vector_store.add_documents(docs)
#     except ValueError as e:
#         # Print the error message
#         print(f"An error occurred: {e}")

#         # Print the stack trace to get more detailed information about where the error occurred
#         traceback.print_exc()


# loader = TextLoader(file_path, encoding="utf-8")
# documents = loader.load()

# MAX_BATCH_SIZE = 5461
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# docs = text_splitter.split_documents(documents)


# print("\n--- Document Chunks Information ---")
# print(f"Number of document chunks: {len(docs)}")
# print(f"Sample chunk:\n{docs[0].page_content}\n")

# print("\n--- Creating vector store ---")


# for i in range(0, len(docs), MAX_BATCH_SIZE):
#     batch = docs[i : i + MAX_BATCH_SIZE]
#     langchain_chroma.add_documents(batch)


loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

vector_store.add_documents(docs)