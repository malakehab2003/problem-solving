entry = input()
entry = entry.split(" ")
x = int(entry[0])
y = int(entry[1])

if x % y == 0 or y % x == 0:
    print("Multiples")
else:
    print("No Multiples")