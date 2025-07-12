entry = int(input())

for i in range(entry):
    num = input()
    num = num[::-1]
    for i in range(len(num)):
        if i == len(num) - 1:
            print(num[i], end='\n')
        else:
            print(num[i], end=" ")