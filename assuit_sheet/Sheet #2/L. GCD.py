def divisor(entry):
    result = []
    for i in range(1, entry + 1):
        if entry % i == 0:
            result.append(i)
    return result

x, y = map(int, input().split())

divisors1 = divisor(x)
divisors2 = divisor(y)

divisors1.reverse()

for i in divisors1:
    if i in divisors2:
        print(i)
        break