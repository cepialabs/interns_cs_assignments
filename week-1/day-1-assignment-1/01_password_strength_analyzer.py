import re

password = input("Enter password: ")
score = 0

if len(password) >= 8:
    score += 1
if re.search("[A-Z]", password):
    score += 1
if re.search("[a-z]", password):
    score += 1
if re.search("[0-9]", password):
    score += 1
if re.search("[@#$%!]", password):
    score += 1

if score >= 4:
    print("Password Strength: STRONG")
elif score == 3:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: WEAK")
