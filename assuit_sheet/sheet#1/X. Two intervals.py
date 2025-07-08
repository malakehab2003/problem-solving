x, i, y, z = map(int, input().split())

if y >= x and y <= i and z >= i:
    print(y, i)
elif y >= x and y <= i and z <= i:
    print(y, z)
elif x >= y and x <= z and z >= i:
    print(x, i)
elif x >= y and x <= z and z <= i:
    print(x, z)
else:
    print(-1)
