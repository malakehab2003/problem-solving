import math

entry = int(input())

years = 0
months = 0
days = 0

if entry >= 365:
    years = math.floor(entry / 365)
    entry = entry - (years * 365)
if entry >= 30:
    months = math.floor(entry / 30)
    entry = entry - (months * 30)

days = entry

print(f"{years} years\n{months} months\n{days} days")