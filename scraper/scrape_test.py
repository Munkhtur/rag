import json
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
from table_format import convert_to_md
from urls import urls
from tqdm import tqdm

# The URL of the webpage you want to scrape
# url = "https://tdbm.mn/mn/retail/bagc-buteegdekhuun/huuhdiin-bagts"
# url = "https://tdbm.mn/mn/retail/savings/hugatsaatai/hugatsaatai-hadgalamj"
# url = "https://tdbm.mn/mn/about-tdbm/introduction"
url = "https://tdbm.mn/mn/retail/savings/hyalbar-hurimtlal"



filename = urlparse(url).path.strip("/").split("/")[-1] + ".md"
# Send a GET request to the website
response = requests.get(url)


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    for calculator_div in soup.find_all("div", class_="field--name-field-calculator"):
        calculator_div.decompose()

    header_content = soup.find("div", class_="field--name-field-body")
    first_content = soup.find( class_="main-content")
    # for i, child in enumerate(first_content.descendants):
    #     print(child)

    return [header_content, first_content]

# Ensure the request was successful (status code 200)
if response.status_code == 200:
    html = response.text
    header , cl_body = clean_body_content(html)
    output =[]
    # Write to a text file
    output.append("# " + header.get_text())
    for child in cl_body.descendants:
        if isinstance(child, str):  
            # If the child is a text node, append its text
            if not child.find_parent('table') and child.strip():  # Check if the parent is not a table
                output.append(child.strip() )
        elif child.name == "table":  # If the child is a table, append its HTML structure
            # output.append(str(child))
            output.append(convert_to_md(str(child)))



    content = "\n".join(output) + "\n" + url + "\n\n"

    with open("./test/" + filename, "w", encoding="utf-8") as file:
        file.write(content)

