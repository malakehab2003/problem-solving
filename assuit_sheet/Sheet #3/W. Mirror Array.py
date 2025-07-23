def swap(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    i, j = 0, m - 1
    while i < m // 2:
        if i == j:
            break
        swap(row, i, j)
        i +=1
        j -=1

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
