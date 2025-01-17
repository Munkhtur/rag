def split_into_parts(input_file_path, output_folder, num_parts=5):
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Split the content into paragraphs (assuming paragraphs are separated by new lines)
    paragraphs = content.split("\n\n")
    total_paragraphs = len(paragraphs)
    
    # Calculate the number of paragraphs per part
    paragraphs_per_part = total_paragraphs // num_parts
    remaining_paragraphs = total_paragraphs % num_parts

    start_idx = 0

    # Split and save into parts
    for i in range(num_parts):
        end_idx = start_idx + paragraphs_per_part + (1 if i < remaining_paragraphs else 0)
        part_content = "\n\n".join(paragraphs[start_idx:end_idx])

        # Save the current part to a file
        output_file_path = f"{output_folder}/part_{i + 1}_test.txt"
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(part_content)

        print(f"Part {i + 1} saved to {output_file_path}")

        start_idx = end_idx

# Example usage
split_into_parts('./books/part_1.txt', './books', num_parts=9)
