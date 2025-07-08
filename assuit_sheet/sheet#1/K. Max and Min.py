entry = input()
entry = entry.split(" ")
x = int(entry[0])
y = int(entry[1])
z = int(entry[2])

min = min(x, min(y, z))
max = max(x, max(y, z))

print(f"{min} {max}")