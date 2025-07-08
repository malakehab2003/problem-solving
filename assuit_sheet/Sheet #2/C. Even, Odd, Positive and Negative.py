noOfNums = int(input())

nums = list(map(int, input().split()))
even = 0
odd = 0
positive = 0
negative = 0


for n in range(noOfNums):
    if nums[n] % 2 == 0:
        even += 1
    else:
        odd += 1
    if nums[n] > 0:
        positive += 1
    elif nums[n] < 0:
        negative += 1

print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")