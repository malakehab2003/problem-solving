import re

entry = input()
pattern = r"\d+\.(0*)"
num = entry.split(".")

if not re.fullmatch(pattern, entry):
    print(f"float {num[0]} 0.{num[1]}")
else:
    print(f"int {num[0]}")