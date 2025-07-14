seat = int(input())

row = seat // 4

if row % 2 != 0:
    col = 3 - (seat % 4)
else:
    col = seat % 4

print(f"{row} {col}")