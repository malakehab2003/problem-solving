entry = input()
entry = entry.split(" ")
unsorted_entry = entry.copy()

entry = list(map(int, entry))
unsorted_entry = list(map(int, unsorted_entry))

entry.sort()
for i in entry:
    print(i)
print("")
for i in unsorted_entry:
    print(i)
