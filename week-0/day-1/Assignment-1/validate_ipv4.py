# Check if input is a valid IPv4 address

def validate_ipv4(address):
    parts = address.split(".")
    if not (len(parts) == 4): return False
    for octet in parts:
        if not (octet.isdigit()): return False
        if len(octet) > 1 and octet[0] == '0': return False
        num = int(octet)
        if not(0 <= num <= 255): return False
    return True
            

if __name__=="__main__":
    ipv4 = input("Enter the IPV4 address: ").strip()
    if validate_ipv4(ipv4):
        print(f"{ipv4} is a valid IPV4 address")
    else:
        print(f"{ipv4} is not a valid IPV4 address")