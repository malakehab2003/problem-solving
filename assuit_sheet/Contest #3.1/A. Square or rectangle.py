tests = int(input())

for _ in range(tests):
    width, height = map(int, input().split())

    if width == height:
        print("Square")
    else:
        print("Rectangle")