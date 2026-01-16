# Search for keyword across multiple log files

def search_keyword_in_logs(file_path, keyword):
    try:
        with open(file_path ,'r') as file:
            for line_number, line in enumerate(file, start=1):
                if keyword.lower() in line.lower(): 
                    print(f"{file_path}:{line_number}: {line.strip()}")
    except FileNotFoundError: 
        print(f"Error: The file {file_path} not found")

if __name__ == "__main__":
    log_file = "application.log"
    keyword = input("Enter the keyword to search: ")
    search_keyword_in_logs(log_file, keyword)