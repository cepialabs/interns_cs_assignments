# Hash a password using SHA-256

import hashlib

def hash_password_sha256(password):
    password_bytes = password.encode()
    hashed = hashlib.sha256(password_bytes).hexdigest()
    print(f"SHA-256 hash: {hashed}")

if __name__ == "__main__":
    password = input("Enter your Password: ").strip()
    hash_password_sha256(password)