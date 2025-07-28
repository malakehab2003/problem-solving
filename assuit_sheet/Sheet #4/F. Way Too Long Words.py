tests = int(input())

for _ in range(tests):
    string = input()

    if len(string) <= 10:
        print(string)
        continue
    print(f"{string[0]}{len(string) - 2}{string[-1]}")