import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching chrome")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)


    try:
        driver.get(website)
        print("page loaded...")
        html = driver.page_source

        time.sleep(10)

        return html
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    for calculator_div in soup.find_all("div", class_="field--name-field-calculator"):
        calculator_div.decompose()

    header_content = soup.find("div", class_="field--name-field-body")
    first_content = soup.find( class_="main-content")

    if not header_content:
        header_content = soup.new_tag("div")  # Create empty div if not found
    if not first_content:
        first_content = soup.new_tag("div")

    # Extract text from first_content except for tables
    for table in first_content.find_all("table"):
        table.insert_before("\n[Table preserved]\n")  # Placeholder text if needed

    # Extract text while preserving tables
    def extract_text_with_tables(element):
        output = []
        for child in element.descendants:
            if child.name == 'table':
                # Capture the HTML of the table, which we want to return as a string
                table_html = str(child)
                output.append(f"\n{table_html}\n")  # Add the table to the parts list (this preserves order)
            else:
                # Extract the text from other elements
                if child.get_text() and not child.find_parent("table"):
                    output.append(child.get_text().strip()) 
        return "\n".join(output)

    first_content_text = extract_text_with_tables(first_content)

    return header_content.get_text(separator="\n") + "\n" + first_content_text

url = "https://tdbm.mn/mn/retail/bagc-buteegdekhuun/tsalingiin-bagts"
html = scrape_website(url)
body = extract_body_content(html)

cl_body = clean_body_content(body)

# Write to a text file
with open("cleaned_content_main_2.txt", "w", encoding="utf-8") as file:
    file.write(str(cl_body))

print("Content saved to cleaned_content.txt")