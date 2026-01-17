import socket

site = input("Enter website: ")

try:
    socket.gethostbyname(site)
    print("Website is reachable")
except:
    print("Website not reachable")
