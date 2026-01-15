# Compare two files using hash

import hashlib

def hash_file(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")

def compare_file_hash(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 is None or hash2 is None:
        return None
    if hash1 != hash2:
        return False
    return True

if __name__=="__main__":
    file1 = input("Enter the path of file1: ").strip()
    file2 = input("Enter the path of file2: ").strip()
    result =  compare_file_hash(file1, file2)
    if result == None:
        print("Cannot Compare files due to missing file(s)")
    elif result:
        print("Files are identical")
    else:
        print("Files are different")