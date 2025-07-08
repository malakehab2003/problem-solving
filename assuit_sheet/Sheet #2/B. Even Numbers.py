entry = int(input())

if entry == 1:
    print("-1")
else:
    for i in range(1, entry + 1):
        if (i) % 2 == 0:
            print(i)
