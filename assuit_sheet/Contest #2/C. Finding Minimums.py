n, k = map(int, input().split())

nums = list(map(int, input().split()))

mins = []
i, group = 0, 0
while i < n:
    min = nums[i]
    while group < k:
        if nums[i] < min:
            min = nums[i]
        group += 1
        i += 1
        if i == n:
            break
    mins.append(min)
    group = 0

for i in mins:
    print(i, end=" ")