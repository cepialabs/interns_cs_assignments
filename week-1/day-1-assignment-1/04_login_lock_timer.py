import shutil
import os

source = input("Enter file to backup: ")
backup_dir = "backup"

os.makedirs(backup_dir, exist_ok=True)

if os.path.exists(source):
    shutil.copy(source, backup_dir)
    print("Backup successful")
else:
    print("File not found")
