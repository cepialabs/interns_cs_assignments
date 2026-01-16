import os

folder = input("Enter folder path: ")

for file in os.listdir(folder):
    if file.endswith(".py"):
        print(file)
