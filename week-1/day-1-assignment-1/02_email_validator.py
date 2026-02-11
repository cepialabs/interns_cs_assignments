import re

email = input("Enter email address: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
