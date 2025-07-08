import math
from decimal import Decimal, ROUND_HALF_UP

entry = input()
entry = entry.split(" ")
x = int(entry[0])
y = int(entry[1])


ceil = math.ceil(x / y)
floor = math.floor(x / y)

div = Decimal(x) / Decimal(y)
round = int(div.to_integral_value(rounding=ROUND_HALF_UP))


print(f"floor {x} / {y} = {floor}")
print(f"ceil {x} / {y} = {ceil}")
print(f"round {x} / {y} = {round}")