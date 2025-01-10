import csv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Function to process the CSV file and invoke the model
def process_csv_and_generate_pairs(csv_file_path, output_csv_path):
    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Use DictReader to access columns by name
        with open(output_csv_path, "w", encoding="utf-8", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["sentence1", "sentence2", "score"])  # Write header
            
            for row in reader:
                news = row["news"]  # Access the "news" column
                
                # Construct the input messages
                messages = [
                    SystemMessage(
                        content="Please create various sentence-score pairs in Mongolian based on the context. Result should be in csv format sentence1,sentence2,score. Score is based on its similairty between 0 and 1. Do not give extra information and extra quotation marks"
                    ),
                    HumanMessage(content=news)
                ]
                
                # Call the model
                result = model.invoke(messages)
                
                # Parse the result and write it to the output CSV
                output_lines = result.content.strip().split("\n")
                for line in output_lines:
                    if line:  # Ensure the line is not empty
                        writer.writerow(line.split(","))  # Split CSV-like results and write to the file
                        
                print(f"Processed news: {news[:50]}...")  # Print progress

# Example usage
input_csv = "./books/sample.csv"  # Replace with the path to your input CSV
output_csv = "./books/output_sentence_pairs.csv"  # Replace with the desired output file path

process_csv_and_generate_pairs(input_csv, output_csv)
