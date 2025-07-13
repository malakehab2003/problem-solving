entry = int(input())

for _ in range(entry):
    x, y = map(int, input().split())
    a = min(x, y)
    b = max(x, y)
    total = b * (b + 1) // 2 - (a - 1) * a // 2
    print(total)