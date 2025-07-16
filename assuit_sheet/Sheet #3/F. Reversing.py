no_of_nums = int(input())

nums = list(map(int, input().split()))

last_index = no_of_nums - 1
for i in range(no_of_nums // 2):
    tmp = nums[i]
    nums[i] = nums[last_index]
    nums[last_index] = tmp
    last_index -= 1

for i in nums:
    print(i, end=" ")