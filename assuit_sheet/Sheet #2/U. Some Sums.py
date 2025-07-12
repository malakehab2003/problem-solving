def suming_of_digits(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

n, a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)
sum = 0

for i in range(1, n + 1):
    sum_of_digits = suming_of_digits(str(i))
    if sum_of_digits >= start and sum_of_digits <= end:
        sum += i

print(sum)