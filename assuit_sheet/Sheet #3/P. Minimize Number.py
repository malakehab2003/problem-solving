n = int(input())

a = list(map(int, input().split()))

count = 0
all_even = True
while True:
    for i in range(n):
        if a[i] % 2 != 0:
            all_even = False
            break
        else:
            a[i] = a[i] // 2
    if not all_even:
        print(count)
        break
    else:
        count += 1
