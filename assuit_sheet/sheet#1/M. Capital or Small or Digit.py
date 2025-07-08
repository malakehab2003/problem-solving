entry = input()

x = ord(entry)

if x >= 48 and x <= 57:
    print("IS DIGIT")
elif x >= 65 and x <= 90:
    print("ALPHA\nIS CAPITAL")
elif x >= 97 and x <= 122:
    print("ALPHA\nIS SMALL")