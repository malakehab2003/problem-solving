array_size = int(input())

array = list(map(int, input().split()))

count = 0

for i in array:
    if (i + 1) in array:
        count += 1

print(count)