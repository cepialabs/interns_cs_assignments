# List files above a certain size

import os

def report_large_files(directory, size):
    try:
      for entry in os.scandir(directory):
         if entry.is_file():
            file_size = os.path.getsize(entry.path)
            if file_size > size:
               size_in_mb = file_size / (1024*1024)
               print(f"{entry.name} - {size_in_mb:.2f} MB")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist")
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'")
if __name__ == "__main__":
    directory = input("Enter the directory to scan for large files: ").strip()
    size = float(input("Enter the size threshold in MB: "))
    filesize_bytes = size * 1024*1024
    report_large_files(directory, filesize_bytes)