import json
import os
from sentence_transformers import InputExample
# Path to the JSON file
file_path = "./books/training_dataset_1.jsonl"

# Load existing data from the JSON file, if it exists
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        train_dataset = json.load(f)

corpus = train_dataset['corpus']
queries = train_dataset['questions']
relevant_docs = train_dataset['relevant_contexts']

examples = []
for query_id, query in queries.items():
    doc_id = relevant_docs[query_id][0]
    text = corpus[doc_id]
    example = InputExample(texts=[query, text])
    examples.append(example)

print(examples[-1])
# # Save the updated dataset back to the file
# with open(file_path, "w") as f:
#     json.dump(existing_data, f, indent=4)



print("Data successfully updated!")

