with open("C:/Users/munkhtur.g/Documents/wikiplaintext/plain_text.txt", "rb") as file:
    content = file.read().decode("utf-8", errors="ignore")

with open("utf8_encoded_file.txt", "w", encoding="utf-8") as outfile:
    outfile.write(content)