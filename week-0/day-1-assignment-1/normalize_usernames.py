# Lowercase and deduplicate usernames

def normalize_usernames(names):
    names_list = names.split(',')
    seen = set()
    normalized = []
    for i, names in enumerate(names_list):
        names_list[i] = names.strip()
    for name in names_list:
        if name.lower() in seen: continue
        normalized.append(name.lower())
        seen.add(name.lower()) 
    with open("normalize_usernames.txt", 'w') as out_file:
        for name in normalized:
            print(name)
            out_file.write(name + "\n")
            

if __name__=="__main__":
    names = input("Enter the list of names seperated by comma: ").strip()
    normalize_usernames(names)