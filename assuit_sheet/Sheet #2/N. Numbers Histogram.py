symbol = input()

noOfNums = int(input())

nums = list(map(int, input().split()))

for i in nums:
    print(symbol * i)
