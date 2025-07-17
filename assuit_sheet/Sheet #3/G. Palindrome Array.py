no_of_nums = int(input())

nums = list(map(int, input().split()))

last_index = no_of_nums - 1

for i in range(no_of_nums):
    if nums[i] != nums[last_index]:
        print("NO")
        exit(0)
    last_index -= 1

print("YES")