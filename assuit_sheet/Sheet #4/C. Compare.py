string1 = input()
string2 = input()

min_string = min(string1, string2)
if min_string == string1:
    max_string = string2
else:
    max_string = string1

for i in range(len(min_string)):
    if min_string[i] > max_string[i]:
        print(max_string)
        exit(0)
    elif min_string[i] < max_string[i]:
        print(min_string)
        exit(0)

print(min_string)