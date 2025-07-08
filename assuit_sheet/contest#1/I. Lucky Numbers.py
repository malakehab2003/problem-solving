entry = input()
no1 = int(entry[0])
no2 = int(entry[1])

if "0" in entry or no1 % no2 == 0 or no2 % no1 == 0:
    print("YES")
else:
    print("NO")
