url = input("Enter URL: ").lower()

keywords = ["login", "secure", "verify"]

for word in keywords:
    if word in url:
        print("Suspicious keyword found:", word)
