import shutil

total, used, free = shutil.disk_usage("/")

print("Free Space:", free // (1024**3), "GB")
