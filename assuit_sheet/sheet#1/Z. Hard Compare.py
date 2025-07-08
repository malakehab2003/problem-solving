import math

x, i, y, z = map(int, input().split())

if (i * math.log(x)) > (z * math.log(y)):
    print("YES")
else:
    print("NO")