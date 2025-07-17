no_of_nums = int(input())

nums = list(map(int, input().split()))

min = nums[0]
min_index = 0
max = nums[0]
max_index = 0

for i in range(no_of_nums):
    if nums[i] < min:
        min = nums[i]
        min_index = i
    if nums[i] > max:
        max = nums[i]
        max_index = i

tmp = min
nums[min_index] = max
nums[max_index] = tmp

for i in nums:
    print(i, end=" ")