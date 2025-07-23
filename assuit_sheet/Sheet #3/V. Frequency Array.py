n, m = map(int, input().split())

a = list(map(int, input().split()))

result = [0 for x in range(1, m + 1)]

for i in a:
    if i <= m:
        result[i - 1] += 1

for i in result:
    print(i)