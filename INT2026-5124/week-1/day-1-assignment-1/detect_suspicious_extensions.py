# Detect dangerous file types in a folder

import os 

def detect_suspicious_extensions(directory, suspicious_exts):
    suspicious_files = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        print(full_path)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in suspicious_exts:
                suspicious_files.append(file)
    if suspicious_files:
        print("Suspicious files found: ")
        for file in suspicious_files:
            print(f"- {file}")
    else:
        print("No suspicious files found in the directory")

if __name__=="__main__":
    directory = input("Enter the directory to check suspicious File: ")
    suspicious_exts = [".bat", ".ps1", ".py"]
    detect_suspicious_extensions(directory, suspicious_exts)