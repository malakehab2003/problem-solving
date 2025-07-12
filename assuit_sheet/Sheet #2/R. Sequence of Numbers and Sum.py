while True:
    no1, no2 = map(int, input().split())

    if no1 <= 0 or no2 <= 0:
        break
    
    sum = 0
    for i in range(min(no1, no2), max(no1, no2) + 1):
        print(i, end=" ")
        sum += i

    print(f"sum ={sum}")