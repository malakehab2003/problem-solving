no_of_nums = int(input())

nums = list(map(int, input().split()))

for i in range(no_of_nums, 0, -1):
    for j in range(i - 1):
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp

for i in nums:
    print(i, end=" ")