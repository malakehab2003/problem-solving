entry = int(input())

nums = list(map(int, input().split()))

sum = 0

for i in nums:
    sum += i

print(abs(sum))