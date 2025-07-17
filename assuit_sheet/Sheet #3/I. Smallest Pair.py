tests = int(input())

for _ in range(tests):
    no_of_nums = int(input())

    nums = list(map(int, input().split()))

    min = nums[0] + nums[1] + 2 - 1
    for i in range(1, no_of_nums):
        for j in range(i + 1, no_of_nums + 1):
            sol = nums[i - 1] + nums[j - 1] + j - i
            if sol < min:
                min = sol

    print(min)