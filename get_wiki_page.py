from sentence_transformers import SentenceTransformer, util

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Grammar rules
grammar_rules = [
    "The letter г indicates two sounds: hoarse г and soft г.",
    "Hoarse г occurs with vowels а, о, у, ы after it.",
    "Soft г occurs without a vowel or with vowels other than а, о, у, ы.",
    "Soft г retains its sound even when suffixes are added."
]

# Encode grammar rules into vectors
rule_embeddings = model.encode(grammar_rules, convert_to_tensor=True)

# Input text
input_text = "хамагаас"
input_embedding = model.encode(input_text, convert_to_tensor=True)

# Calculate similarity
cosine_scores = util.pytorch_cos_sim(input_embedding, rule_embeddings)

# Get the most relevant rule
most_relevant_idx = cosine_scores.argmax()
print(f"Relevant Grammar Rule: {grammar_rules[most_relevant_idx]}")
