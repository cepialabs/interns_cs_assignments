# Check if URL starts with http or https

def check_url_scheme(url):        
    if url.startswith("http://"):
        print(f"{url} starts with http")
    elif url.startswith("https://"):
        print(f"{url} starts with https")
    else:
        print("Invalid URL")

if __name__=="__main__":
    url = input("Enter the URL: ").strip()
    check_url_scheme(url)