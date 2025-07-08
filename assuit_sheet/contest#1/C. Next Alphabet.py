entry = input()

if ord(entry) == 122:
    print(chr(97))
else:
    print(chr(ord(entry) + 1))