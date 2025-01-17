import time
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import tqdm
import json
import os
from langchain_community.document_loaders import TextLoader


# Setup environment variables and messages
# load_dotenv(override=True)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "part_15.txt")

# persistent_directory = os.path.join(current_dir, "db", "chroma_db_mongoltxt_110")


if not os.path.exists(file_path):
    raise FileNotFoundError(
        f"The file {file_path} does not exist. Please check the path."
    )

# Read the text content from the file
loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=100, length_function=len
)

training_documents = text_splitter.split_documents(loader.load())
print("---", len(training_documents))
import uuid

id_set = set()

for document in training_documents:
    id = str(uuid.uuid4())
    while id in id_set:
        id = uuid.uuid4()
    id_set.add(id)
    document.metadata["id"] = id


qa_chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyCUUezOQ1gAosXWDR4vOgzvR7fcDzVyDHQ")


qa_prompt = """\
Given the following context, you must generate questions in Mongolian based on only the provided context.
Do not include any explanation or translation.
You are to generate {n_questions} questions which should be provided in the following format:

1. QUESTION #1
2. QUESTION #2
...

Context:
{context}
"""


qa_prompt_template = ChatPromptTemplate.from_template(qa_prompt)

question_generation_chain = qa_prompt_template | qa_chat_model


def create_questions_safe(documents, n_questions, file_path):
    # Load existing data from the JSON file, if it exists

    # Initialize with an empty dataset structure

    for document in tqdm.tqdm(documents[200:]):
        existing_data = {"questions": {}, "relevant_contexts": {}, "corpus": {}}

        questions = existing_data.get("questions", {})
        relevant_docs = existing_data.get("relevant_contexts", {})
        corpus = existing_data.get("corpus", {})
        try:
            questions_generated = question_generation_chain.invoke(
                {"context": document.page_content, "n_questions": n_questions}
            )
            for question in questions_generated.content.split("\n"):
                question_id = str(uuid.uuid4())
                if question.strip():
                    questions[question_id] = "".join(question.split(".")[1:]).strip()
                    relevant_docs[question_id] = [document.metadata["id"]]
            # Add document to the corpus
            corpus[document.metadata["id"]] = document.page_content
            save_to_file(file_path, questions, relevant_docs, corpus)
            time.sleep(4)
        except Exception as e:
            print(f"Error encountered: {e}")
            # Save progress to file in case of an error
            # save_to_file(file_path, questions, relevant_docs, corpus)
            continue  # Skip the problematic document and continue

    # Final save after processing all documents
    # save_to_file(file_path, questions, relevant_docs, corpus)


def save_to_file(file_path, questions, relevant_docs, corpus):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing_data = json.load(f)
    else:
        # Initialize with an empty dataset structure
        existing_data = {"questions": {}, "relevant_contexts": {}, "corpus": {}}

    ex_questions = existing_data.get("questions", {})
    ex_relevant_docs = existing_data.get("relevant_contexts", {})
    ex_corpus = existing_data.get("corpus", {})

    ex_questions.update(questions)
    ex_relevant_docs.update(relevant_docs)
    ex_corpus.update(corpus)

    with open(file_path, "w") as f:
        json.dump(existing_data, f)


# Call the function
file_path = "./books/mongol_data_eval.jsonl"
create_questions_safe(training_documents, 5, file_path)
