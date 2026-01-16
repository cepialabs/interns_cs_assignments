# Count occurrences of “ERROR” in log files

def count_error_logs(file_path):
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                count += line.upper().count("ERROR")
        print(f"Error occured {count} times in the log file {file_path}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")

if __name__ == "__main__":
    log_file = "application.log"
    count_error_logs(log_file)