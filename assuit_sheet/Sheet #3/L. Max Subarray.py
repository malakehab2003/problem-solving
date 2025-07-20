tests = int(input())

for _ in range(tests):
    no_of_nums = int(input())

    nums = list(map(int, input().split()))

    i = 0
    j = 1
    max_int = []
    while j <= no_of_nums:
        while i + j <= no_of_nums:
            sub_array = nums[i:i + j]
            max_int.append(max(sub_array))
            i += 1
        i = 0
        j += 1

    # print array with spaces between elements
    # last element with new line
    for i in range(len(max_int)):
        if i == len(max_int) -1:
            print(max_int[i])
            break
        print(max_int[i], end=" ")
