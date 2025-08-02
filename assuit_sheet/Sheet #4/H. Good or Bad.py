tests = int(input())

for _ in range(tests):
    string = input()
    if "010" in string or "101" in string:
        print("Good")
    else:
        print("Bad")