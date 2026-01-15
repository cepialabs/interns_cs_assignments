# Verify internet connectivity

import platform
import subprocess

def check_internet_connection():
    host = "8.8.8.8"
    is_windows = platform.system().lower() == 'windows'
    if is_windows:
        ping_cmd = ["ping", "-n", "1", host]
    else:
        ping_cmd = ["ping", "-c", "1", host]
    try:
        result = subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        if is_windows:
            if "unreachable" in output.lower() or "timed out" in output.lower():
                return False
            return True
        else:
            if result.returncode != 0:
                return False
            return True
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

if __name__ == "__main__":
    if check_internet_connection():
        print("Internet is reachable")
    else:
        print("Internet is unreachable")