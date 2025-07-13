n = int(input())

level = 1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * level)
    level += 2

for i in range(n, 0, -1):
    level -= 2
    print(" " * (n - i), end="")
    print("*" * level)