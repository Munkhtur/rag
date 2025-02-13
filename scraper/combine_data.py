import os
import glob
import json

# Define the path pattern
data_path = "./data/*/final_data.json"

# List to store all JSON data
combined_data = []

# Loop through each final_data.json file
for file_path in glob.glob(data_path):
    print(f"Processing: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            combined_data.extend(data)  # Assuming data is a list
        except json.JSONDecodeError as e:
            print(f"Error reading {file_path}: {e}")

# Save combined JSON data
output_file = "combined_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print(f"Combined JSON saved to {output_file}")