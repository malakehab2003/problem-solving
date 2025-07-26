n = int(input())

array = list(map(int, input().split()))

for i in range(n):
    if array[i] == 0:
        subarray = array[0:i].copy()
        subarray = reversed(subarray)
        array[0:i] = subarray

for i in array:
    print(i, end=" ")
