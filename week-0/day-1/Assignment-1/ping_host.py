#  Ping a host and check reachability
import platform
import subprocess

def ping_host(host):
    is_windows = platform.system().lower() == 'windows'
    if is_windows:
        ping_cmd = ["ping", "-n", '1', host]
    else:
        ping_cmd = ["ping", "-c", '1', host]
    try:
        result = subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        print(output)
        if is_windows:
            if "unreachable" in output.lower() or "timed out" in output.lower():
                print(f"{host} is NOT reachable")
            else:
                print(f"{host} is reachable")
        else:
            if result.returncode == 0:
                print(f"{host} is reachable")
            else:
                print(f"{host} is not reachable")
    except Exception as e:
        print(f"An error occured when pinging {e}")


if __name__ == "__main__":
    host = input("Enter the hostname or IP to ping: ").strip()
    ping_host(host)