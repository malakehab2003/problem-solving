array_size, sum_nums = map(int, input().split())

array = list(map(int, input().split()))

array.sort(reverse=True)

sum = 0
for i in range(sum_nums):
    if array[i] > 0:
        sum += array[i]

print(sum)