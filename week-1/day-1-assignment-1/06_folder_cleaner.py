import os

folder = input("Enter folder path: ")

for file in os.listdir(folder):
    if file.endswith(".tmp"):
        os.remove(os.path.join(folder, file))
        print("Deleted:", file)
