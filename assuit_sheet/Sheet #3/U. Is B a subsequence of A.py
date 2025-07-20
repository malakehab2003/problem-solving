n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

for i in b:
        if i not in a:
            print("NO")
            exit(0)
        else:
            a = a[a.index(i) + 1:]
        
print("YES")