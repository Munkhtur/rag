import os

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import FireCrawlLoader


# Load environment variables from .env
load_dotenv(override=True)

# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "db")
# persistent_directory = os.path.join(db_dir, "chroma_db_mobicom")

api_key = os.getenv("FIRECRAWL_API_KEY")
if not api_key:
    raise ValueError("FIRECRAWL_API_KEY environment variable not set")

# Step 1: Crawl the website using FireCrawlLoader
print("Begin crawling the website...")
loader = FireCrawlLoader(
        api_key=api_key, url="https://tdbm.mn/mn/retail/savings/hugatsaatai/hugatsaatai-hadgalamj", mode="scrape")
documents = loader.load()
print("Finished crawling the website.")
for doc in documents:
    for key, value in doc.metadata.items():
        if isinstance(value, list):
            doc.metadata[key] = ", ".join(map(str, value))
output_file = "crawled_documents_tdb_page.txt"

# Open the file in write mode
with open(output_file, "w", encoding="utf-8") as f:
    for doc in documents:
        # Write the document content
        f.write("Content:\n")
        f.write(doc.page_content)
        f.write("\n\n")
        
        # Write the metadata
        f.write("Metadata:\n")
        for key, value in doc.metadata.items():
            f.write(f"{key}: {value}\n")
        
        # Add a separator for readability
        f.write("\n" + "="*50 + "\n\n")

print(f"Crawled documents saved to {output_file}")

# Step 2: Split the scraped content into chunks
# CharacterTextSplitter splits the text into smaller chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)

# Display information about the split documents
# print("\n--- Document Chunks Information ---")
# print(f"Number of document chunks: {len(docs)}")
# print(f"Sample chunk:\n{docs[0].page_content}\n")

# Step 3: Create embeddings for the document chunks
# OpenAIEmbeddings turns text into numerical vectors that capture semantic meaning
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-mpnet-base-v2"
# )

# Step 4: Create and persist the vector store with the embeddings
# Chroma stores the embeddings for efficient searching
# if not os.path.exists(persistent_directory):
#     print(f"\n--- Creating vector store in {persistent_directory} ---")
#     db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)
#     print(f"--- Finished creating vector store in {persistent_directory} ---")
# else:
#     print(f"Vector store {persistent_directory} already exists. No need to initialize.")
#     db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

# Step 5: Query the vector store
# Create a retriever for querying the vector store
# retriever = db.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 3},
# )

# Define the user's question
# query = "Евент"

# # Retrieve relevant documents based on the query
# relevant_docs = retriever.invoke(query)

# Display the relevant results with metadata
# print("\n--- Relevant Documents ---")
# for i, doc in enumerate(relevant_docs, 1):
#     print(f"Document {i}:\n{doc.page_content}\n")
#     if doc.metadata:
#         print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")