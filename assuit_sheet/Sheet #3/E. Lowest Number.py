no_of_nums = int(input())

nums = list(map(int, input().split()))

min = nums[0]
for i in range(no_of_nums):
    if nums[i] < min:
        min = nums[i]

print(min, nums.index(min) + 1)