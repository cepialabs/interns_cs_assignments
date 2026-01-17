text = input("Enter message: ")
encrypted = ""

for char in text:
    encrypted += chr(ord(char) + 2)

print("Encrypted:", encrypted)
