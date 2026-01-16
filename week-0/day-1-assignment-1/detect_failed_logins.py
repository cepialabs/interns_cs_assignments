# Parse log for failed login attempts

def detect_failed_logins(log_file):
    failed_login_attempts = []
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if "failed" in line.lower():
                    failed_login_attempts.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File {log_file} does not exist")
        exit()
    return failed_login_attempts
    
if __name__=="__main__":
    log_file = "login.log"
    failed_attempts = detect_failed_logins(log_file)
    if failed_attempts: 
        print(f"Found {len(failed_attempts)} failed login attempts")
        for attempt in failed_attempts:
            print(f"- {attempt}")
    else:
        print("No failed login attempts found")