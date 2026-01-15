# Detect World-Writable Permission Files

import os 
import stat

def detect_world_writable_files(directory):
    print("\nScanning for world-writable files...\n")
    insecure_files = []
    try: 
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try: 
                    file_stat = os.stat(file_path)
                    if file_stat.st_mode & stat.S_IWOTH:
                        insecure_files.append(file_path)
                except PermissionError:
                    continue
    except FileNotFoundError:
        print("Error: Directory does not exist")
        return None
    return insecure_files

if __name__=="__main__":
    directory = input("Enter the directory: ").strip()
    insecure_files = detect_world_writable_files(directory)
    if insecure_files is None:
        pass
    elif insecure_files:
        print("World-Writable Files Found: ")
        for file in insecure_files:
            print(f"- {file}")
    else:
        print("No World Writable Files Found")