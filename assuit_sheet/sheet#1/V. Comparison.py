entry = input()
entry = entry.split(" ")
num1 = int(entry[0])
num2 = int(entry[2])
sign = entry[1]

if sign == ">" and num1 > num2:
    print("Right")
elif sign == "<" and num1 < num2:
    print("Right")
elif sign == "=" and num1 == num2:
    print("Right")
else:
    print("Wrong")
