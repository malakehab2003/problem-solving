entry = input()
entry = entry.split(" ")
x = float(entry[0])
y = float(entry[1])

if x == 0:
    if y == 0:
        print("Origem")
    else:
        print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0:
    if y > 0:
        print("Q1")
    else:
        print("Q4")
else:
    if y > 0:
        print("Q2")
    else:
        print("Q3")

