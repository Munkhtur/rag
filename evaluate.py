from sentence_transformers import SentenceTransformer, evaluation

# Load the model
model = SentenceTransformer("gmunkhtur/paraphrase-multilingual-minilm-l12-v3-mn")

# Prepare evaluation data
sentences1 = [
    "Тэд “Зэрлэг цэцэгсийн хүлэмж” кино хийсэн",
    "Тэдний хоёр дахь бүтээл “Зүрхээр наадагч” кино юм."
]
sentences2 = [
    "Тэдний хоёр дахь бүтээл “Зүрхээр наадагч” кино юм.",
    "Францын агуу дуучин эмэгтэй Эдит Пиаф."
]
scores = [0.8, 0.2]  # Ground truth similarity scores

# Define the evaluator
evaluator = evaluation.EmbeddingSimilarityEvaluator(sentences1, sentences2, scores)

# Run evaluation
result = evaluator(model)
print("Pearson Correlation:", result["pearson"])
print("Spearman Correlation:", result["spearman"])


from scipy.stats import pearsonr, spearmanr
import numpy as np

# Generate embeddings
embeddings1 = model.encode(sentences1)
embeddings2 = model.encode(sentences2)

# Compute cosine similarities
cosine_similarities = np.array([
    np.dot(e1, e2) / (np.linalg.norm(e1) * np.linalg.norm(e2))
    for e1, e2 in zip(embeddings1, embeddings2)
])

# Calculate correlations
pearson_corr, _ = pearsonr(cosine_similarities, scores)
spearman_corr, _ = spearmanr(cosine_similarities, scores)

print("Pearson Correlation:", pearson_corr)
print("Spearman Correlation:", spearman_corr)


import matplotlib.pyplot as plt

plt.scatter(scores, cosine_similarities, alpha=0.5)
plt.xlabel("Ground Truth Scores")
plt.ylabel("Predicted Similarities")
plt.title("Similarity Prediction vs Ground Truth")
plt.grid(True)
plt.show()


for i, (gt, pred, s1, s2) in enumerate(zip(scores, cosine_similarities, sentences1, sentences2)):
    if abs(gt - pred) > 0.3:  # Significant difference
        print(f"Pair {i}:")
        print(f"  Sentence 1: {s1}")
        print(f"  Sentence 2: {s2}")
        print(f"  Ground Truth: {gt}")
        print(f"  Predicted: {pred}")
