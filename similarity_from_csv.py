from sentence_transformers import SentenceTransformer, util
import csv
# Load model
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Test sentences
import re

# Load the book text file
file_path = "./books/cleaned_file_3.csv"

# with open(file_path, "r", encoding="utf-8") as f:
#     text = f.read()

# # Split text into sentences (basic regex for splitting by punctuation)
# sentences = re.split(r'(?<!\w\.\w.)(?<![А-Я][а-я]\.)(?<=\.|\?)\s', text)

# Print sentences


output_file = './books/sentence_similarity_results_3.csv'

def process_csv_and_generate_pairs(csv_file_path, output_csv_path):
    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file,delimiter=";")  # Use DictReader to access columns by name
        with open(output_csv_path, "w", encoding="utf-8", newline="") as output_file:
            writer = csv.writer(output_file, delimiter=";")
            writer.writerow(["sentence1", "sentence2", "score"])  # Write header
# Calculate and print similarity scores
            for row in reader:
                sent1 = row["sentence1"]
                sent2 = row["sentence2"]
                print(sent2)
                
                # Encode sentences
                embedding1 = model.encode(sent1, convert_to_tensor=True)
                embedding2 = model.encode(sent2, convert_to_tensor=True)

                # Calculate cosine similarity
                similarity = util.pytorch_cos_sim(embedding1, embedding2).item()

                # Write sentence pair and similarity score to the CSV file immediately
                writer.writerow([sent1, sent2, similarity])

            # Optionally print progress every 1000 iterations
        
process_csv_and_generate_pairs(file_path, output_file)
print(f"Results have been written to {output_file}")