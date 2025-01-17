import os
import time

from langchain.text_splitter import RecursiveCharacterTextSplitter

# from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from tqdm import tqdm
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_core.documents.base import Document


load_dotenv(override=True)


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "part_1.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongol_context")
# db = Chroma(
#     persist_directory=persistent_directory,
#     embedding_function=HuggingFaceEmbeddings(
#         model_name="gmunkhtur/finetuned_paraphrase-multilingual"
#     ),
# )


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

if not os.path.exists(file_path):
    raise FileNotFoundError(
        f"The file {file_path} does not exist. Please check the path."
    )

# Read the text content from the file
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Split the content into paragraphs (assuming paragraphs are separated by new lines)
paragraphs = content.split("\n\n")
# 2447
print("-------------------", len(paragraphs))
total = 0
for paragraph in tqdm(paragraphs, desc="Processesing pragraphs"):
    document = [Document(page_content=paragraph)]

    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(document)
    print("docs----",len(docs))
    total += len(docs)
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

    # for chunk in tqdm(docs, desc="processeing chuncks"):
    #     context = add_context_chain.invoke(
    #         {"chunk": chunk.page_content, "document": document[0].page_content}
    #     )
    #     if context:
    #         chunk.page_content += "\n" + context
    #     time.sleep(4)
    # embeddings = HuggingFaceEmbeddings(
    #     model_name="gmunkhtur/finetuned_paraphrase-multilingual"
    # )

    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it automatically
    print("\n--- Creating vector store ---")
    # db.add_documents(docs)
    print("\n--- Finished creating vector store ---")

print("total", total)