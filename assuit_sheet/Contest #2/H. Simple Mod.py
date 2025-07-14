import math

n = int(input())

limit = 10**6

for x in range(0, limit + 1):
    x2 = x * x
    rem = (-x2) % n

    y = int(math.isqrt(rem))
    if (y * y) % n == rem:
        print(x, y)
        break
else:
    print("No solutions")