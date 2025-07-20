n = int(input())

fib = [0, 1]

for i in range(3, n + 1):
    fib.append(fib[i - 2] + fib[i - 3])

print(fib[n - 1])