x, y = map(int, input().split())

if (x != 0 and y != 0) and \
    (x == y or x - y == 1 or y - x == 1):
    print("YES")
else:
    print("NO")