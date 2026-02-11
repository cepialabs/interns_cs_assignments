from datetime import datetime

with open("log.txt", "a") as file:
    file.write(str(datetime.now()) + "\n")

print("Log updated")
