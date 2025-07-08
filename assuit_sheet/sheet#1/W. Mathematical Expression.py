entry = input()
entry = entry.split(" ")
num1 = int(entry[0])
num2 = int(entry[2])
sign = entry[1]
result = int(entry[4])

if sign == "+":
    if(num1 + num2) == result:
        print("Yes")
    else:
        print(num1 + num2)

if sign == "-":
    if(num1 - num2) == result:
        print("Yes")
    else:
        print(num1 - num2)

if sign == "*":
    if(num1 * num2) == result:
        print("Yes")
    else:
        print(num1 * num2)