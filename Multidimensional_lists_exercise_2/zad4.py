Coordinate = tuple[int, int]

size: int = int(input())
field: list[list[str]] = [list(input().split()) for _ in range(size)]

bunny_field_position: Coordinate = next((row, col) for row in range(len(field))
                                        for col in range(len(field[0]))
                                        if field[row][col] == "B")

directions: dict[str, Coordinate] = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
}

max_eggs_collected: float = -float("inf")
best_direction: str = ""
best_path: list[list[int]] = []

for direction, (dr, dc) in directions.items():
    eggs_collected: int = 0
    r, c = bunny_field_position
    path: list[list[int]] = []

    while True:
        r, c = r + dr, c + dc

        if not (0 <= r < size and 0 <= c < size) or field[r][c] == "X":
            break

        eggs_collected += int(field[r][c])
        path.append([r, c])

    if max_eggs_collected < eggs_collected and path:
        max_eggs_collected = eggs_collected
        best_direction = direction
        best_path = [row[:] for row in path]

print(best_direction)
[print(row) for row in best_path]
print(max_eggs_collected)