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
            writer = csv.writer(output_file,delimiter=";")
            writer.writerow(["sentence1", "sentence2"])  # Write header
            
            for row in reader:
                news = row["news"]  # Access the "news" column
                
                # Construct the input messages
#                    SystemMessage(
#                         content=(
# "Create various sentence pairs in Mongolian based on the context. Ensure these pairs include a mix of:"
# "1. Highly similar pairs: Paraphrased sentences that retain the same intent and meaning."
# "2. Moderately similar pairs: Sentences with partial overlap in meaning or related but different information."
# "3. Dissimilar pairs: Sentences that are unrelated or contradict the original meaning."

# "Generate diverse paraphrased versions that generalize or specify the query while keeping the intent intact. Include:"
# "- Varied formulations, such as direct questions, incomplete phrases, and specific inquiries."
# "- Common misspellings or informal word usage."
# "- Diverse sentence structures to enhance robustness."

# "Output the results in clean CSV format as `sentence1;sentence2`. Use `;` as the delimiter and avoid including scores, additional explanations, or non-sentence text."

#                         )
#                         ),
                messages = [
                    SystemMessage(content=(
                        "Create various sentence pairs in Mongolian based on the context. Ensure a mix of highly similar, similar and dissimilar pairs. Generate paraphrased versions that generalize, specify, or diversify the query. Include:"
                        "1. Direct paraphrases."
                        "2. Diverse sentence structures (questions, statements, and incomplete phrases)."
                        "3. Deliberate misspellings or typos."
                        "4. Broader and tangential generalizations."
                        "Format the output in CSV with `sentence1;sentence2`. Avoid including scores or extra information."
                        "mix of similar and dissimilar pairs can be understood in terms of semantic similarity, syntactic structure, and meaning alignment"
                    )),
                    HumanMessage(content=news)
                ]
                
                # Call the model
                result = model.invoke(messages)
                
                # Parse the result and write it to the output CSV
                output_lines = result.content.strip().split("\n")
                for line in output_lines:
                    if line:  # Ensure the line is not empty
                        writer.writerow(line.split(";"))  # Split CSV-like results and write to the file
                        
                print(f"Processed news: {news[:50]}...")  # Print progress

# Example usage
input_csv = "./books/split_file_3.csv"  # Replace with the path to your input CSV
output_csv = "./books/pair_result3.csv"  # Replace with the desired output file path

process_csv_and_generate_pairs(input_csv, output_csv)
