no_of_nums = int(input())

nums = list(map(int, input().split()))

target = int(input())

for i in range(no_of_nums):
    if nums[i] == target:
        print(i)
        exit(0)
print(-1)