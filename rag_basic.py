import os

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.retrievers.document_compressors import flashrank_rerank #FlashrankRerank
from langchain.retrievers import ContextualCompressionRetriever
# from langchain_openai import OpenAIEmbeddings
from langchain_cohere import CohereRerank
from dotenv import load_dotenv
load_dotenv(override=True)


# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db_mpnet")

# Define the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)

# Load the existing vector store with the embedding function
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# Define the user's question
query = "Дорноговь аймаг"

# Retrieve relevant documents based on the query
# retriever = db.as_retriever( 
#     search_type="similarity_score_threshold",
#     search_kwargs={"k":3, "score_threshold": 0.5},
# )

# retriever = db.as_retriever(
#     search_type="mmr",
#     search_kwargs={"k": 10, "fetch_k": 20, "lambda_mult":0.1},
# )
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k":3},
)

# compressor = CohereRerank(model="rerank-multilingual-v2.0")

# # compressor = flashrank_rerank.FlashrankRerank()
# compression_retriever = ContextualCompressionRetriever(
#     base_compressor=compressor, base_retriever=retriever
# )
# relevant_docs = compression_retriever.invoke(query)
relevant_docs = retriever.invoke(query)

# Display the relevant results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")