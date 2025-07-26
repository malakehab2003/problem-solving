array_size = int(input())

array = list(map(int, input().split()))

count1 = 0
for i in range(array_size):
    if i % 2 == 0:
        if array[i] < 0:
            count1 += 1
    else:
        if array[i] > 0:
            count1 += 1

count2 = 0
for i in range(array_size):
    if i % 2 == 0:
        if array[i] > 0:
            count2 += 1
    else:
        if array[i] < 0:
            count2 += 1

print(min(count1, count2))