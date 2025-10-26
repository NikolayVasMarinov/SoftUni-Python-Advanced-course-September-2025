def valid_coordinates(r: int, c: int, matrix_size: int) -> bool:
    return 0 <= r < matrix_size and 0 <= c < matrix_size

size: int = int(input())

matrix: list[list[int]] = [list(map(int, input().split())) for _ in range(size)]

bomb_coordinates: list[tuple[int, int]] = [(int(r), int(c)) for coordinates in input().split()
                                           for r, c in [coordinates.split(",")]]


for current_bomb in bomb_coordinates:
    r, c = current_bomb

    if matrix[r][c] <= 0:
        continue

    cells_affected = [
        (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
        (r, c - 1), (r, c + 1),
        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)

    ]

    for row, column in cells_affected:
        if not valid_coordinates(row, column, size) or matrix[row][column] <= 0:
            continue

        matrix[row][column] -= matrix[r][c]

    matrix[r][c] = 0

alive_cells: list[int] = [cell for row in matrix for cell in row if cell > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(*row)