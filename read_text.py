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