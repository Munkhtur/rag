import psycopg2
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "part_1.txt")
# Establish a connection to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres", 
    password="123456", 
    host="localhost", 
    port="5432"
)


loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Create a cursor
cur = conn.cursor()
cur.execute('SET search_path TO textsearch;')

# Insert documents (chunks) into the table
for doc in docs:
    cur.execute("INSERT INTO documents (content) VALUES (%s)", (doc.page_content,))

# Commit changes and close the cursor
conn.commit()
cur.close()
conn.close()
