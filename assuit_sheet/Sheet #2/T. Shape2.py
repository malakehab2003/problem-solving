n = int(input())

level = 1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * level)
    level += 2