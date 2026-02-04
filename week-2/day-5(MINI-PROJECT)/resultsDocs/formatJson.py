import json

# Load JSON file
with open("crt.sh.json", "r") as f:
    data = json.load(f)

subdomains = set()  # unique subdomains

for entry in data:
    names = entry.get("name_value", "").split("\n")
    for name in names:
        subdomains.add(name.strip())  # remove extra spaces

# Save cleaned list
with open("crtsh-dmce-clean.txt", "w") as f:
    for sub in sorted(subdomains):
        f.write(sub + "\n")

print(f"Total unique subdomains: {len(subdomains)}")