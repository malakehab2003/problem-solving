n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

x = int(input())

for i in matrix:
    if x in i:
        print("will not take number")
        exit(0)

print("will take number")