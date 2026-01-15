# Ensure port is in 0–65535 range

def validate_port_number(port_number):
    if not port_number.isdigit(): return False
    port = int(port_number)
    if not 0 <= port <= 65535: return False
    return True  

if __name__=="__main__":
    port_number = input("Enter the port number: ").strip()
    if validate_port_number(port_number):
        print(f"{port_number} is a valid port number")
    else:
        print(f"{port_number} is not a valid port number")