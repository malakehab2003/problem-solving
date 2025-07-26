def get_input():
    row, col = map(int, input().split())

    matrix = []
    for _ in range(row):
        r = list(input().strip())
        matrix.append(r)

    x, y = map(int, input().split())

    return (matrix, x - 1, y - 1, row, col)


if __name__ == '__main__':
    matrix, x, y, row, col = get_input()

    directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]
    
    all_x = True

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < row and 0 <= ny < col:
            if matrix[nx][ny] != 'x':
                all_x = False
                break
    print("yes" if all_x else "no")
    