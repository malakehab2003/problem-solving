string = input()

i = 0
j = len(string) - 1
while i <= j:
    if string[i] != string[j]:
        print("NO")
        exit(0)
    i += 1
    j -= 1

print("YES")