import json
import os
from sentence_transformers import InputExample
# Path to the JSON file
# file_path = "./scraper/data/eval.jsonl"
# # file_path_res = "./books/result.json"
# output_file = "./cohere_eval.jsonl"  
# # Load existing data from the JSON file, if it exists
# train_dataset = []
# if os.path.exists(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             train_dataset.append(json.loads(line.strip()))

# corpus = train_dataset[0]['corpus']  # Assuming the corpus is the same for all examples
# queries = train_dataset[0]['questions']  # Assuming questions are the same for all examples
# relevant_docs = train_dataset[0]['relevant_contexts'] 
# print(len(queries))
# examples = []
# for query_id, query in queries.items():
#     doc_id = relevant_docs[query_id][0]
#     text = corpus[doc_id]
#     example = {"query":query, "relevant_passages": [text]}
#     examples.append(example)

# # print(len(queries))
# with open(output_file, "w", encoding="utf-8") as f:
#     for entry in examples:
#         json.dump(entry, f, ensure_ascii=False)
#         f.write("\n")

# print(f"Question and relevant document pairs saved to {output_file}!")


print("Data successfully updated!")


#########################################

import cohere

co = cohere.ClientV2("IQdhjcAu6onsC4g7upMNNvvM11zlcMc7MsPzFhcV")

rerank_dataset_with_eval = co.datasets.create(
    name="rerank-dataset-with-eval",
    data=open("./cohere_train.jsonl", "rb"),
    eval_data=open("./filtered_chohere_eval.jsonl", "rb"),
    type="reranker-finetune-input",
)

response = co.wait(rerank_dataset_with_eval)
print(response)
# print(rerank_dataset_with_eval.await_validation())


# with open("cohere_train.jsonl", "r", encoding="utf-8") as f:
#     train_data = [json.loads(line.strip()) for line in f]

# # Extract queries from the train dataset
# train_queries = set(entry["query"] for entry in train_data)

# # Load the eval dataset
# with open("cohere_eval.jsonl", "r", encoding="utf-8") as f:
#     eval_data = [json.loads(line.strip()) for line in f]
# filtered_eval_data = [entry for entry in eval_data if entry["query"] not in train_queries]
# with open("filtered_chohere_eval.jsonl", "w", encoding="utf-8") as f:
#     for entry in filtered_eval_data:
#         json.dump(entry, f, ensure_ascii=False)
#         f.write("\n")  # Write each entry on a new line

# print(f"Filtered eval dataset saved to 'filtered_chohere_eval.jsonl'")