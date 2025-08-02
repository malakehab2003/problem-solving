string = input()

result = {}

for i in string:
    if i not in result.keys():
        result[i] = 1
    else:
        result[i] += 1

sorted_dict = dict(sorted(result.items()))
    
for key, value in sorted_dict.items():
    print(f"{key} : {value}")