tests = int(input())

for _ in range(tests):
    s1, s2 = input().split()

    min_len = min(len(s1), len(s2))

    result = ""
    for i in range(min_len):
        result += s1[i]
        result += s2[i]

    result += s1[min_len:] + s2[min_len:]
    print(result)