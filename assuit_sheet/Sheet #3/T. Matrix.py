n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))

    matrix.append(row)

i, j = 0, 0
primary_diagonal = 0
secondary_diagonal = 0
while i < n  and j < n:
    primary_diagonal += matrix[i][j]
    secondary_diagonal += matrix[i][n - j - 1]
    i += 1
    j += 1

print(abs(primary_diagonal - secondary_diagonal))