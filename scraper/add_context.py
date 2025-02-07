from pathlib import Path
import re
import time
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_core.documents.base import Document
from langchain_core.output_parsers import StrOutputParser


load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Define a function to preserve tables during splitting
def preserve_tables_in_chunks(content, chunk_size=1000, chunk_overlap=128):
    # Regex to identify tables in markdown
    table_regex = r"(\|.*\|(\n\|.*\|)+)"
    
    # Step 1: Identify all tables and replace them with placeholders
    tables = []
    table_counter = 0
    def replace_table_with_placeholder(match):
        nonlocal table_counter
        table_counter += 1
        tables.append(match.group(0))  # Store the table
        return f"{{table_{table_counter}}}"  # Placeholder for the table
    
    # Replace tables with placeholders
    content_with_placeholders = re.sub(table_regex, replace_table_with_placeholder, content)
    
    # Step 2: Split the rest of the document normally
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_text(content_with_placeholders)
    
    # Step 3: Reassemble the chunks with tables intact
    for i, chunk in enumerate(chunks):
        for j, table in enumerate(tables):
            chunk = chunk.replace(f"{{table_{j+1}}}", table)  # Replace placeholders with actual tables
        chunks[i] = chunk  # Reassign the modified chunk
    
    return chunks

# Load the Markdown file
document_path = Path("./savings-formated.md")
loader = UnstructuredMarkdownLoader(document_path)
print("------------loading-----------------")
loaded_docs = loader.load()

# Assuming loaded_docs contains the entire markdown content
content = loaded_docs[0].page_content  # Accessing the correct attribute


# Print the chunks (or write to a new file)
contextual_prompt = """
        <document>
        {document}
        </document>

        Please provide a summary of the document in a few paragraphs in Mongolian. 
        If different pieces of information in the document are related, combine them into one coherent context. 
        The summary should be informative and concise, and it should cover all major topics of the document, consolidating related details into a single paragraph where appropriate.
          This summary will be used to improve retrieval in a RAG (Retrieval-Augmented Generation) setup. So the genereted paragraphs supposed to look like part of the document.
        """

contextual_prompt = PromptTemplate.from_template(contextual_prompt)

add_context_chain = contextual_prompt | llm | StrOutputParser()
output_file_path = "./saving-context.md"
with open(output_file_path,"w", encoding="utf-8") as output_file:

    context = add_context_chain.invoke(
        { "document": content}
    )
    if context:
        content += "\nContext: " + context
    output_file.write(content)
    # time.sleep(4)