# Detect duplicate lines in a log

def find_duplicate_lines(file_path):
    seen = set()
    duplicate_lines_count = 0
    total_lines_processed = 0
    output_file_name = "find_duplicate_lines.txt"
    
    try:
        with open(output_file_name, 'w') as out_file:
            with open(file_path, 'r') as file:
                for line in file:
                    total_lines_processed += 1
                    if line.lower().strip() in seen:
                        out_file.write(line.strip() + "\n")
                        duplicate_lines_count += 1
                    else: seen.add(line.lower().strip())
        print("Summary: ")
        print("Total lines processed:", total_lines_processed)
        print("Number of duplicate lines found:", duplicate_lines_count)
        print("Duplicates saved in:", output_file_name)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")


if __name__ == "__main__":
    log_file = "application.log"
    find_duplicate_lines(log_file)