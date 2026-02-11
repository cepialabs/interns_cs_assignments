import os

file = input("Enter filename: ")

if os.path.exists(file):
    size = os.path.getsize(file)
    print("File size:", size, "bytes")
else:
    print("File not found")
