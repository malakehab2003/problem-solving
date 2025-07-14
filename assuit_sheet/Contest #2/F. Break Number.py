entry = int(input())
nums = list(map(int, input().split()))

divids = []
for i in nums:
    count = 0
    while i % 2 == 0:
        count += 1
        i = i // 2
    divids.append(count)

print(max(divids))