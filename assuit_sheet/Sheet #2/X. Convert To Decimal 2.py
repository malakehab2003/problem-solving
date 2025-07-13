entry = int(input())

for _ in range(entry):
    n = int(input())
    ones_count = bin(n).count('1')
    result = (1 << ones_count) - 1
    print(result)