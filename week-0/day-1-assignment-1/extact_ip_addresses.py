# Extract all IPs from logs

import re
def extract_ip_addresses(file_path):
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ip_addresses = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                matches = re.findall(ip_pattern, line)
                for ip in matches:
                    parts = ip.split(".")
                    if all(0 <= int(part) <= 255 for part in parts):
                        ip_addresses.append(ip)
        unique_ips = set(ip_addresses)
        print("Unique IP addresses:")
        for ip in unique_ips:
            print(ip)
        with open("extract_ip_addresses.txt", 'w') as out_file:
            for ip in unique_ips:
                out_file.write(ip + "\n")    
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

if __name__ == "__main__":
    log_file = "application.log"
    extract_ip_addresses(log_file)