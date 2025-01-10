# with open("./books/split_file_1.csv", "r", encoding="utf-8", errors="replace") as file:
#     content = file.read()

# with open("./books/split_file_1_fixed.csv", "w", encoding="utf-8") as file:
#     file.write(content)

import chardet

file_path = "./books/split_file_1.csv"
output_path = "./books/split_file_1_clean_replaced_2.csv"

with open(file_path, "rb") as file:
    content = file.read()

# Replace the problematic byte (0x81) with an obvious marker
replacement_marker = b"###"
problematic_byte = 0x81

# Replace all instances of the problematic byte
modified_content = content.replace(bytes([problematic_byte]), replacement_marker)

# Save the modified content to a new file
with open(output_path, "wb") as file:
    file.write(modified_content)

print(f"Problematic bytes replaced with '{replacement_marker.decode()}' and saved to {output_path}.")


# with open("./books/split_file_1.csv", "rb") as file:
#     content = file.read()
#     problematic_byte = 0x81  # Replace this with the byte you're looking for
#     context_range = 10
#     for idx, byte in enumerate(content):
#         if byte == problematic_byte:
#             start = max(0, idx - context_range)
#             end = min(len(content), idx - 1 + context_range)
#             surrounding_bytes = content[start:end]
            
            
#             try:
#                 surrounding_text = surrounding_bytes.decode("utf-8")
#             except UnicodeDecodeError:
#                 surrounding_text = surrounding_bytes.decode("utf-8", errors="replace")
            
#             print(f"Problematic byte found at position {idx}:")
#             print(f"Surrounding text: {surrounding_text}")
#             print(f"Hex view: {surrounding_bytes.hex()}")
#             break  # Remove this line if you want to find all occurrences