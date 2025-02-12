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
from tqdm import tqdm
import argparse
import os
from langchain.document_loaders import TextLoader


load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def add_context_to_all(folder_path, topic):
    save_directory = f"./data/{topic}/context/"
    os.makedirs(save_directory, exist_ok=True)

    markdown_files = Path(folder_path).glob("*.md")
    for file_path in  tqdm(markdown_files):
# Define a function to preserve tables during splitting
# Load the Markdown file
        filename = os.path.basename(file_path)
        output_path = save_directory + filename

# Create the directory if it doesn't exist
        
        # loader = UnstructuredMarkdownLoader(file_path=file_path, )
        # print("------------loading-----------------" , file_path)
        # loaded_docs = loader.load()

        # Assuming loaded_docs contains the entire markdown content
        # content = loaded_docs[0].page_content  # Accessing the correct attribute
        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()

        content = documents[0].page_content        
        # Print the chunks (or write to a new file)
        contextual_prompt = """
                <document>
                {document}
                </document>
                Background: Provided document is part of webpage of Trade and Development Bank of Mongolia. 
                Please provide a summary of the document in a few paragraphs in Mongolian. 
                If different pieces of information in the document are related, combine them into one coherent context. 
                The summary should be informative and concise, and it should cover all major topics of the document, consolidating related details into a single paragraph where appropriate.
                This summary will be used to improve retrieval in a RAG (Retrieval-Augmented Generation) setup. So the genereted paragraphs supposed to look like part of the document.
                """

        contextual_prompt = PromptTemplate.from_template(contextual_prompt)

        add_context_chain = contextual_prompt | llm | StrOutputParser()
        # output_file_path = "./saving-context.md"
        with open(output_path,"w", encoding="utf-8") as output_file:

            context = add_context_chain.invoke(
                { "document": content}
            )
            if context:
                paragraphs = content.split("\n")
                paragraphs.insert(-1, "\n" + context)
                content = "\n".join(paragraphs)
            output_file.write(content)
            time.sleep(4)

parser = argparse.ArgumentParser(description='Process URLs for a given topic.')
parser.add_argument('topic', type=str, help='The topic to process')
args = parser.parse_args()
topic = args.topic


directory = f"./data/{topic}/raw/"

add_context_to_all(directory, topic)