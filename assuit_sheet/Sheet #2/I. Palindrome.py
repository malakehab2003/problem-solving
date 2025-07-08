entry = input()

reverse = entry[::-1]

print(int(reverse))
if entry == reverse:
    print("YES")
else:
    print("NO")