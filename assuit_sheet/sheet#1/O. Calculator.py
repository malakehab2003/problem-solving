entry = input()

if "+" in entry:
    entry = entry.split("+")
    print(int(entry[0]) + int(entry[1]))
elif "-" in entry:
    entry = entry.split("-")
    print(int(entry[0]) - int(entry[1]))
elif "*" in entry:
    entry = entry.split("*")
    print(int(entry[0]) * int(entry[1]))
elif "/" in entry:
    entry = entry.split("/")
    print(int(int(entry[0]) / int(entry[1])))