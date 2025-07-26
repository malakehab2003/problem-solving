n, q = map(int, input().split())

a = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + a[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l - 1])