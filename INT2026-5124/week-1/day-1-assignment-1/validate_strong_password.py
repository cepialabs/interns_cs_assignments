# Check password strength

def validate_strong_password(password):
    if not (len(password)>=8): return False
    if not any(ch.isupper() for ch in password): return False
    if not any(ch.islower() for ch in password): return False
    if not any(ch.isdigit() for ch in password): return False
    special_chars = "!@#$%^&*()-_+=<>?/.,:"
    if not any(ch in special_chars for ch in password): return False
    return True 

if __name__=="__main__":
    password = input("Enter the password: ").strip()
    if validate_strong_password(password):
        print("Strong Password")
    else:
        print("Weak Password")