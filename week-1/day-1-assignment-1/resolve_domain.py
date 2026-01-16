# Resolve a domain name to its IP

import socket

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        print("Could not resolve the domain name")
        exit()
    print(f"The IP Address of {domain} is {ip_address}")

if __name__ == "__main__":
    domain = input("Enter the domain to resolve: ").strip()
    resolve_domain(domain)
