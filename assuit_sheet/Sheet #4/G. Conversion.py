string = input()

string = string.replace(",", " ")
result = ""
for i in range(len(string)):
    if string[i].isupper():
        result += string[i].lower()
    elif string[i].islower():
        result += string[i].upper()
    else:
        result += string[i]
print(result)