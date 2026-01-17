filename = input("Enter text file: ")

with open(filename) as f:
    words = f.read().split()

print("Total words:", len(words))
