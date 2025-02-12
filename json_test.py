import json
import os
from sentence_transformers import InputExample
# Path to the JSON file
file_path = "./scraper/data/training_data.jsonl"
# file_path_res = "./books/result.json"
output_file = "./sample_pairs_3.txt"  
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

print(len(queries))
with open(output_file, "w", encoding="utf-8") as out_file:
    for query_id, query in queries.items():
        # Get the relevant document using the query_id
        doc_id = relevant_docs[query_id][0]
        text = corpus[doc_id]
        
        # Write the question and relevant document pair in a readable format
        out_file.write(f"Question: {query}\n")
        out_file.write(f"Relevant Document: {text}\n")
        out_file.write("-" * 50 + "\n")  # Divider between each pair

print(f"Question and relevant document pairs saved to {output_file}!")


print("Data successfully updated!")

