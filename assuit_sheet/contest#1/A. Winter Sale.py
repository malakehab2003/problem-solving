x, y = map(int, input().split())

result = float((100 * y) / (100 - x))

formatted = "{:.2f}".format(result)
print(formatted)