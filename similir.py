from sentence_transformers import SentenceTransformer, util
import csv
# Load model
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Test sentences
import re

# Load the book text file
file_path = "./books/utf8_encoded_file.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Split text into sentences (basic regex for splitting by punctuation)
sentences = re.split(r'(?<!\w\.\w.)(?<![А-Я][а-я]\.)(?<=\.|\?)\s', text)

# Print sentences
for sentence in sentences[:5]:
    print(sentence , "----")

positive_pairs = [(sentences[i], sentences[i+1]) for i in range(len(sentences) - 1)]

print(positive_pairs[0])
scored_pairs = []

output_file = 'sentence_similarity_results.csv'

with open(output_file, mode='w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Sentence 1", "Sentence 2", "Similarity Score"])
# Calculate and print similarity scores
    for i in range(len(sentences) - 1):
            sent1 = sentences[i]
            sent2 = sentences[i + 1]
            
            # Encode sentences
            embedding1 = model.encode(sent1, convert_to_tensor=True)
            embedding2 = model.encode(sent2, convert_to_tensor=True)

            # Calculate cosine similarity
            similarity = util.pytorch_cos_sim(embedding1, embedding2).item()

            # Write sentence pair and similarity score to the CSV file immediately
            writer.writerow([sent1, sent2, similarity])

        # Optionally print progress every 1000 iterations
            if i % 1000 == 0:
                print(f"Processed {i+1} sentence pairs...")

print(f"Results have been written to {output_file}")