tests = int(input())

for _ in range(tests):
    array_size = int(input())

    array = list(map(int, input().split()))

    if array_size % 2 != 0:
        print(-1)
        continue
    even_count = 0
    for i in array:
        if i % 2 == 0:
            even_count += 1
        
    result = abs((array_size // 2) - even_count)
    print(result)
