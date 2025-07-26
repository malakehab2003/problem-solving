array_size = int(input())

array = list(map(int, input().split()))

front, end = 0, array_size - 1

while front <= end:
    if front == end:
        print(array[front], end=" ")
        break
    print(array[front], end=" ")
    print(array[end], end=" ")
    front += 1
    end -= 1
