import random
import time

otp = random.randint(100000, 999999)
print("OTP:", otp)

time.sleep(5)

user = int(input("Enter OTP: "))

if user == otp:
    print("OTP Verified")
else:
    print("OTP Expired or Invalid")
