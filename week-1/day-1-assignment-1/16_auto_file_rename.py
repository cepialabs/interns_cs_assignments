import os

path = input("Enter folder path: ")

for i, file in enumerate(os.listdir(path)):
    os.rename(
        os.path.join(path, file),
        os.path.join(path, f"file_{i}.txt")
    )
print("Files have been renamed.")