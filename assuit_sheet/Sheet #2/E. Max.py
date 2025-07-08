noOfNums = int(input())

nums = list(map(int, input().split()))

max = nums[0]
for num in range(noOfNums):
    if nums[num] > max:
        max = nums[num]

print(max)