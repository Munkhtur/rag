from sentence_transformers import SentenceTransformer

model_1 = SentenceTransformer("sentence-transformers/paraphrase-multilingual-minilm-l12-v2")
model_2 = SentenceTransformer("intfloat/multilingual-e5-large")


test_data = [
    ("Тэр ном уншсан уу?", "Тэр номыг үзсэн үү?", 0.9),
    ("Би ажилдаа явна.", "Би гэртээ байна.", 0.1)
]


from sklearn.metrics.pairwise import cosine_similarity

def evaluate_model(model, data):
    predictions = []
    ground_truth = []

    for text1, text2, label in data:
        emb1 = model.encode(text1, convert_to_tensor=True)
        emb2 = model.encode(text2, convert_to_tensor=True)
        similarity = cosine_similarity(emb1.reshape(1, -1), emb2.reshape(1, -1))[0][0]
        predictions.append(similarity)
        ground_truth.append(label)

    return predictions, ground_truth


from scipy.stats import spearmanr

pred_1, gt = evaluate_model(model_1, test_data)
pred_2, _ = evaluate_model(model_2, test_data)

corr_1 = spearmanr(pred_1, gt).correlation
corr_2 = spearmanr(pred_2, gt).correlation

print(f"Model 1 Spearman Correlation: {corr_1}")
print(f"Model 2 Spearman Correlation: {corr_2}")


query = "Монгол улсын төрийн далбаа"
documents = [
    "Монгол улсын төрийн далбааг үндэсний баяр болгон тэмдэглэдэг.",
    "Төрийн далбааны өдөр нь ардын хувьсгалтай холбоотой.",
    "Спортын арга хэмжээний талаар мэдээлэл өгье."
]

query_embedding = model_1.encode(query)
doc_embeddings = model_1.encode(documents)

# Rank documents by cosine similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0]
ranked_docs = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)
for doc, score in ranked_docs:
    print(f"Score: {score:.4f} | Document: {doc}")

