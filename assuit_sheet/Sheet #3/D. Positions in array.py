no_of_nums = int(input())

nums = list(map(int, input().split()))

for i in range(no_of_nums):
    if nums[i] <= 10:
        print(f"A[{i}] = {nums[i]}")