import re

x, y = map(int, input().split())
regex = r'[47]+'
exists = False

for i in range(x, y + 1):
    if re.fullmatch(regex, str(i)):
        print(i, end=" ")
        exists = True

if not exists:
    print(-1)