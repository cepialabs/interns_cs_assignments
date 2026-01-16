# Scan a list of ports and report open ones

import socket

def port_scanner(host, ports, timeout=1):
    print(f"Starting Port Scanning on {host}")
    print(f"Scanning {len(ports)} ports...\n")
    open_ports =  []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            result = sock.connect_ex((host,port))
            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)
        except socket.error:
            pass
        finally:
            sock.close()
    print("\nScan Complete")
    if open_ports:
        print("Open ports found: ", open_ports)
    else:
        print("No Open Ports found")
        

if __name__ == "__main__":
    target_host = input("Enter host: ").strip()
    common_ports = [
        21,    # FTP
        22,    # SSH
        23,    # Telnet
        25,    # SMTP
        53,    # DNS
        80,    # HTTP
        110,   # POP3
        443    # HTTPS
    ]

    port_scanner(target_host, common_ports)