tests = int(input())

for _ in range(tests):
    no_of_nums = int(input())

    nums = list(map(int, input().split()))

    i = 0
    j = 1
    count = 0
    while j <= no_of_nums:
        while i + j <= no_of_nums:
            sub_array = nums[i:i + j]
            if sub_array == sorted(sub_array):
                count += 1
            i += 1
        i = 0
        j += 1

    
    print(count)
