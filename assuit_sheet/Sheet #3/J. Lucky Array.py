no_of_nums = int(input())

nums = list(map(int, input().split()))

min = min(nums)
count = nums.count(min)

if count % 2 == 0:
    print("Unlucky")
    exit(0)
print("Lucky")