import os
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import Qdrant
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from llama_parse import LlamaParse
import asyncio
import numpy as np
from uuid import uuid4
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, losses
from langchain.embeddings.base import Embeddings


load_dotenv()

def create_database(pdf_path: str, db_path: str, collection_name: str):
    print("-------------begin --------------------")
    # Set up the parsing instruction
    instruction = """
        The provided document is an annual report of a bank, written in Mongolian. The document contains financial statements, management discussions, tables, graphs, and strategic insights.  
        Your task is to analyze this document and extract all its content in full detail without summarizing. Ensure that all text, tables, and graphs are accurately represented in their original form.  
        The result should be in Mongolian and maintain the structure, language, and format of the original document as closely as possible. Focus on ensuring that tables and graphs are clearly presented and described.  
        Do not include recuring page header and page number.
        Avoid condensing or omitting any part of the document, ensuring a complete and faithful reproduction of its content.
       Focus on ensuring that tables and graphs are presented clearly and consistently using Markdown formatting, with proper alignment of columns and rows for better readability.  
    """

    # Initialize the parser
    parser = LlamaParse(
        api_key=os.getenv("PARSER_KEY"),
        result_type="markdown",
        # parsing_instruction=instruction,
        max_timeout=5000,
        language="mn",
        content_guideline_instruction=instruction,
    )

    # Parse the document

    
    llama_parse_documents = parser.load_data(pdf_path)
    print(len(llama_parse_documents), "----------")
    parsed_doc = llama_parse_documents[0]

    print(parsed_doc, "+++++++++")
    markdown_file_path = os.path.join(db_path, f"{collection_name}.md")

    with open(markdown_file_path, "w", encoding="utf-8") as file:
        for doc in llama_parse_documents:
            file.write(doc.text)


create_database("../books/AR-23.pdf", "../books", "ar-23-2" )