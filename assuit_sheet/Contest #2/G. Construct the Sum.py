def print_to_n(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()


def get_sum_to_n(n):
     sum_all_nums = (n * (n + 1)) / 2
     return sum_all_nums


def print_nums_in_array(nums):
    for i in nums:
        print(i, end=" ")
    print()


def print_numbers_to_s(n, s):
    sum = 0
    nums = []
    for i in range(n, 0, -1):
        if i + sum <= s:
            sum += i
            nums.append(i)
        if sum == s:
            break
    print_nums_in_array(nums)


entry = int(input())

for _ in range(entry):
    n, s = map(int, input().split())

    # remove bigger numbers
    if n > s:
         n = s - 1

    # get summition of all numbers
    sum_all_nums = get_sum_to_n(n)

    # print -1 if sum is smaller than s
    # print all nums if sum equal s
    if sum_all_nums < s:
        print(-1)
    elif sum_all_nums == s:
        print_to_n(n)
    else:
        
        print_numbers_to_s(n, s)
            
    