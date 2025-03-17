from sentence_transformers import SentenceTransformer

model_id = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
model = SentenceTransformer(model_id)

print(model.summary())