entry = int(input())

for i in range(entry):
    for j in range(entry):
        if i == entry // 2 and j == entry // 2:
            print("X", end="")
        elif j - i == 0:
            print("\\", end="")
        elif i + j == entry - 1:
            print("/", end="")
        else:
            print("*", end="")
    print()