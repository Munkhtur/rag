import pandas as pd

# Load both CSV files
csv1 = pd.read_csv("./books/sentence_similarity_results_3.csv",delimiter=";")
csv2 = pd.read_csv("./books/combined.csv",delimiter=";")

# Concatenate them (stack rows)
combined = pd.concat([csv1, csv2], ignore_index=True)

# Save to a new CSV
combined.to_csv("./books/combined_2.csv", index=False, sep=";")
