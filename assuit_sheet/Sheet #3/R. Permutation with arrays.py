n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in a:
    if i not in b:
        print("no")
        exit(0)
    else:
        b.remove(i)

print("yes")