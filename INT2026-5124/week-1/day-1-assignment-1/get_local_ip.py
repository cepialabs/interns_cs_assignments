# Fetch the local IP of the machine

import socket

def get_local_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    local_ip = sock.getsockname()[0]  # Returns tuple (local_ip, local_port)
    sock.close()
    print(f"Local IP Address: {local_ip}")

if __name__ == "__main__":
    get_local_ip()