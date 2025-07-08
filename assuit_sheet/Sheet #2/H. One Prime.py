entry = int(input())

halfNum = entry // 2
prime = True

if entry == 1:
    prime = False
    print("NO")

for i in range(2, entry - halfNum + 1):
    if entry % i == 0:
        prime = False
        print("NO")
        break
if prime:
    print("YES")