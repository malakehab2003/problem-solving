x, y, z = map(int, input().split())

if x % z == 0 and y % z == 0:
    print("Both")
elif x % z == 0:
    print("Memo")
elif y % z == 0:
    print("Momo")
else:
    print("No One")