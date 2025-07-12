entry = int(input())

game = 1
for i in range(entry):
    for i in range(4):
        if game % 4 != 0:
            print(game, end=" ")
            game += 1
    print("PUM")
    game += 1
    