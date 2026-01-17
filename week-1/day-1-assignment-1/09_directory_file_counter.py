import os

path = input("Enter directory: ")

files = os.listdir(path)
print("Total files:", len(files))
