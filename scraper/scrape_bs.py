import json
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
from table_format import convert_to_md
from urls import urls
from tqdm import tqdm
import argparse
import os
import markdownify


# The URL of the webpage you want to scrape
# url = "https://tdbm.mn/mn/retail/bagc-buteegdekhuun/huuhdiin-bagts"
# url = "https://tdbm.mn/mn/retail/savings/hugatsaatai/hugatsaatai-hadgalamj"
# url = "https://tdbm.mn/mn/about-tdbm/introduction"
# url = "https://tdbm.mn/mn/about-tdbm/rewards"
parser = argparse.ArgumentParser(description='Process URLs for a given topic.')
parser.add_argument('topic', type=str, help='The topic to process')
args = parser.parse_args()
topic = args.topic

for i, urlset in enumerate(tqdm( urls[topic])):
    path = urlparse(urlset[0]).path.strip("/").split("/")
    filename = f"{i}-{path[-1] if path[-1] else 'index'}.md"
    content = ""
    for url in urlset:
        print(url)
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
            # for child in cl_body.descendants:
            #     if isinstance(child, str):  
            #         # If the child is a text node, append its text
            #         if not child.find_parent('table') and child.strip():  # Check if the parent is not a table
            #             output.append(child.strip() )
            #     elif child.name == "table":  # If the child is a table, append its HTML structure
            #         # output.append(str(child))
            #         # output.append(convert_to_md(str(child)))
            #         output.append( markdownify.markdownify(str(child), heading_style="ATX") )
            output.append( markdownify.markdownify(str(cl_body), heading_style="ATX") )

        content += "\n".join(output)
        

    content +="\n" + urlset[0] + "\n\n"
    directory = f"./data/{topic}/raw"

    os.makedirs(directory, exist_ok=True)

    with open("./data/"+ topic +"/raw/"+ filename, "w", encoding="utf-8") as file:
        file.write(content)

