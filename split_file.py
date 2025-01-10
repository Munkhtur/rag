import pandas as pd

# Load the CSV file
input_file = "C:/Users/munkhtur.g/Downloads/eduge.csv"
output_file_base = "./books/split_file_"

# Read the CSV into a DataFrame
df = pd.read_csv(input_file)

# Calculate the number of rows per split
total_rows = len(df)
rows_per_file = total_rows // 10

# Split and save into separate files
for i in range(10):
    start_idx = i * rows_per_file
    # For the last file, include all remaining rows
    end_idx = (i + 1) * rows_per_file if i < 9 else total_rows
    split_df = df.iloc[start_idx:end_idx]
    split_df.to_csv(f"{output_file_base}{i+1}.csv", index=False)

print("CSV file split into 5 parts!")
