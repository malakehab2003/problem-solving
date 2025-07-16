no_of_nums = int(input())

nums = list(map(int, input().split()))

for i in range(no_of_nums):
    if nums[i] > 0:
        nums[i] = 1
    elif nums[i] < 0:
        nums[i] = 2

for i in nums:
    print(i, end=" ")
