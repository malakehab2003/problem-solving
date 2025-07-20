import re

a, b = map(int, input().split())
s = input()

pattern = r'^\d+-\d+$'
if re.fullmatch(pattern, s) and s[a] == '-':
    print('Yes')
    exit(0)
print("No")
