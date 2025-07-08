def is_prime(entry):
    halfNum = entry // 2

    if entry == 1:
        return False

    for i in range(2, entry - halfNum + 1):
        if entry % i == 0:
            return False
    return True

entry = int(input())

for i in range(2, entry + 1):
    if is_prime(i):
        print(i, end=" ")