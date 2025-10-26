MOVEMENT: dict[str, tuple[int, int]] = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
}

size: int = int(input())
field: list[list[str]] = []

pacman_position: tuple[int, int]
health: int = 100
total_stars: int = 0
immunity: bool = False

for r in range(size):
    line = list(input())
    field.append(line)

    for c in range(size):
        if field[r][c] == "P":
            pacman_position = (r, c)

        if field[r][c] == "*":
            total_stars += 1



while True:
    command = input()

    if command == "end":
        print("Pacman failed to collect all the stars.")
        break

    dr, dc = MOVEMENT[command]
    nr, nc = pacman_position[0] + dr, pacman_position[1] + dc

    if nr >= size:
        nr = nr - size

    elif nr < 0:
        nr = size + nr

    if nc >= size:
        nc = nc - size

    elif nr < 0:
        nc = size + nc


    field[pacman_position[0]][pacman_position[1]] = "-"

    if field[nr][nc] == "G":
        if immunity:
            immunity = False
        else:
            health -= 50

    elif field[nr][nc] == "F":
        immunity = True

    elif field[nr][nc] == "*":
        total_stars -= 1

    field[nr][nc] = "P"
    pacman_position = (nr, nc)

    if total_stars == 0:
        print("Pacman wins! All the stars are collected.")
        break

    if health == 0:
        print(f"Game over! Pacman last coordinates [{nr},{nc}]")
        break

print(f"Health: {health}")

if total_stars > 0:
    print(f"Uncollected stars: {total_stars}")

for row in field:
    print(*row, sep="")