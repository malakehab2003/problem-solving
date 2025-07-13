entry = int(input())

fib = [0, 1]
for i in range(2, entry + 1):
    fib.append(fib[i - 1] + fib[i - 2])

for i in range(entry):
    print(fib[i], end=" ")