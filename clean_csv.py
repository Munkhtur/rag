import pandas as pd

# Step 1: Load the CSV file with the correct delimiter
df = pd.read_csv('./books/pair_result3.csv', delimiter=';')

# Step 2: Clean up any extra spaces or unwanted characters in columns
df['sentence1'] = df['sentence1'].str.replace('"""', '', regex=False).str.strip()
df['sentence2'] = df['sentence2'].str.replace('"""', '', regex=False).str.strip()

# Step 3: Remove any rows that are empty (if any)
df = df.dropna(subset=['sentence1', 'sentence2'])

# Step 4: Remove any remaining extra spaces in columns (if needed)
df['sentence1'] = df['sentence1'].str.strip()
df['sentence2'] = df['sentence2'].str.strip()


# Step 5: Save the cleaned data back to a new CSV file
df.to_csv('./books/cleaned_file_3.csv', index=False, sep=';')

# Check the cleaned data
print(df.head())
