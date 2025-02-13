from io import StringIO
import json
import os
import traceback
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from tqdm import tqdm
from dotenv import load_dotenv
from dataclasses import dataclass, field
import time
import argparse
from pathlib import Path
from typing import Dict, List

# @dataclass
# class DocumentData(Dict):
#     context: str
#     chunks: List[str]
load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

contextual_prompt = """\
    <document>
    {document}
    </document>
    Here is the chunk we want to situate within the whole document
    <chunk>
    {chunk}
    </chunk>
    Please give a short succinct context in Mongolian to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else.
    """

contextual_prompt = PromptTemplate.from_template(contextual_prompt)

add_context_chain = contextual_prompt | llm | StrOutputParser()

def add_context_to_chunks(folder_path, topic, file_name):
    save_directory = f"./data/{topic}/"
    output_file = os.path.join(save_directory, "additional_data.json")
    os.makedirs(save_directory, exist_ok=True)
    file_path = f"./data/{topic}/context/{file_name}"
    all_chunks = []

    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    last_paragraph = documents[0].page_content.strip().split("\n")[-1]
    document_content = documents[0].page_content
    paragraphs = document_content.split("\n")
    paragraphs = paragraphs[:-1]  # Remove the last paragraph

    # Reassemble the text without the last paragraph
    documents[0].page_content = "\n".join(paragraphs)

    # doc = {
    #     "context" : documents[0].page_content if documents else "",
    #     "chunks" : []
    # }
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )
        docs = text_splitter.split_documents(documents)

        for chunk in tqdm(docs, desc="processeing chuncks"):
            context = add_context_chain.invoke(
                    {"chunk": chunk.page_content, "document": documents[0].page_content}
                    )
            if context:
                chunk.page_content += "\n" + context
            time.sleep(4)
            # last_paragraph = documents[0].page_content.strip().split("\n")[-1]
        
            chunk_data = {"chunk": chunk.page_content, "source": last_paragraph}
            
            all_chunks.append(chunk_data)

    except ValueError as e:
        # Print the error message
        print(f"An error occurred: {e}")

        # Print the stack trace to get more detailed information about where the error occurred
        traceback.print_exc()

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(all_chunks, outfile, ensure_ascii=False, indent=4)

parser = argparse.ArgumentParser(description='Process URLs for a given topic.')
parser.add_argument('topic', type=str, help='The topic to process')
parser.add_argument('file', type=str, help='The topic to process')
args = parser.parse_args()
topic = args.topic
file = args.file

directory = f"./data/{topic}/context/{file}"


add_context_to_chunks(directory, topic, file)