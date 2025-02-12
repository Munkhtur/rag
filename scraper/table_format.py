
import tqdm
import json
import os
from bs4 import BeautifulSoup







# qa_chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


# qa_prompt = """\

# Context:
# {table}
# """


# qa_prompt_template = ChatPromptTemplate.from_template(qa_prompt)

# question_generation_chain = qa_prompt_template | qa_chat_model

def convert_to_md(html_table):
    soup = BeautifulSoup(html_table, "html.parser")
    
    # Extract table headers
    headers = soup.find_all("th")
    # if len(headers) >0:
    header_row = []
    for header in headers:
        colspan = int(header.get("colspan", 1))  # Get colspan if available
        header_text = header.get_text(strip=True)
        header_row.extend([header_text] * colspan)  # Repeat for colspan
    
    # Start with the header row
    md_table = "|" + "|".join(header_row) + "|\n"
    
    # Create a separator for the headers
    md_table += "|" + "|".join(["---"] * len(header_row)) + "|\n"
    
    # Extract table rows and format them
    if len(headers) >0:

        rows = soup.find_all("tr")[1:]  # Skip the header row
    else:
        rows = soup.find_all("tr")  # Skip the header row

    for row in rows:
        cells = row.find_all("td")
        md_row = []
        
        for cell in cells:
            colspan = int(cell.get("colspan", 1))  # Get colspan for each cell
            cell_text = cell.get_text(strip=True)
            md_row.extend([cell_text] * colspan)  # Repeat cell text based on colspan
        
        md_table += "|" + "|".join(md_row) + "|\n"
    
    return md_table
    # else:
    #     return soup.get_text()

# # Call the function
# file_path = "./data/training_dataset_eval.jsonl"
# # create_questions_safe(training_documents, 5, file_path)
# modified_lines = []
# file_path = "./savings.md"
# with open(file_path, 'r', encoding='utf-8') as file:
#     lines = file.readlines()  # Read all lines into a list
#     for line in lines:
#         if line.startswith("<table"):
#             converted_table = convert_to_md(line)  # Convert the table to markdown format
#             modified_lines.append(converted_table)  # Append the converted table
#         else:
#             modified_lines.append(line) 

# with open("./savings-formated.md", 'w', encoding='utf-8') as file:
#     file.writelines(modified_lines)