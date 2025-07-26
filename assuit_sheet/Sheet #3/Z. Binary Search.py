def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for _ in range(q):
    x = int(input())
    if binary_search(a, x):
        print("found")
    else:
        print("not found")

    