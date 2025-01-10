# Import the required tokenizer classes (replace with actual class names)
from transformers import AutoTokenizer

# Initialize both tokenizers
mongolian_tokenizer = AutoTokenizer.from_pretrained("gmunkhtur/tokenizer_mn")  # Assuming you have a Mongolian-specific tokenizer
# mongolian_tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/paraphrase-multilingual-minilm-l12-v2")  # Assuming you have a Mongolian-specific tokenizer

# Define the Mongolian text to test
mongolian_text = "орос хэлний хүчтэй хүрээлэлд байгаа буриад, халимаг, өвөрмонголчууд"
print(f"Mongolian Text: {mongolian_text}\n")

# Test Mongolian tokenizer
print("Using Mongolian Tokenizer:")
mongolian_encoded_ids = mongolian_tokenizer.encode(mongolian_text)
print(f"Encoded Ids: {mongolian_encoded_ids}")
mongolian_decoded_text = mongolian_tokenizer.decode(mongolian_encoded_ids)
print(f"Decoded Text: {mongolian_decoded_text}\n")


print(mongolian_tokenizer.convert_ids_to_tokens(mongolian_encoded_ids))


print(mongolian_tokenizer.vocab_size)
len(mongolian_tokenizer)

# Check vocabulary size
print("Vocabulary size:", mongolian_tokenizer.vocab_size)

# Inspect special tokens
print("Special tokens:", mongolian_tokenizer.all_special_tokens)

# Test tokenization for a Mongolian sentence
sample_sentence = "Сайн байна уу?"
tokens = mongolian_tokenizer.tokenize(sample_sentence)
print("Tokens:", tokens)
print("Token IDs:", mongolian_tokenizer.convert_tokens_to_ids(tokens))