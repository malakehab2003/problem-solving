n, k, a = map(int, input().split())

value = n * k

if value % a != 0:
    print("double")
elif value // a < 2147483648:
    print("int")
else:
    print("long long")
