rows, columns = map(int, input().split(", "))
game_map: list[list[str]] = []

bomb_coordinates: tuple[int, ...] = tuple()
player_coordinates: tuple[int, ...] = tuple()

MOVEMENT: dict[str, tuple[int, int]] = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
}

time_left: int = 16

for r in range(rows):
    line = list(input())
    game_map.append(line)

    for c in range(columns):
        character: str = game_map[r][c]

        if character == "C":
            player_coordinates = (r, c)

        elif character == "B":
            bomb_coordinates = (r, c)

nr, nc = player_coordinates

while True:

    if time_left <= 0:
        print("Terrorists win!\nBomb was not defused successfully!"
              "\nTime needed: 0 second/s.")
        game_map[nr][nc] = "*"
        break

    action = input()

    if action == "defuse":
        if bomb_coordinates == (nr, nc):
            time_left -= 4

            if time_left >= 0:
                game_map[nr][nc] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {time_left} second/s remaining.")

            else:
                game_map[nr][nc] = "X"
                print("Terrorists win!\nBomb was not defused successfully!"
                      f"\nTime needed: {-time_left} second/s.")

            break

        else:
            time_left -= 2
            continue


    time_left -= 1

    dr, dc = MOVEMENT[action]

    if not (0 <= nr + dr < rows and 0 <= nc + dc < columns):
        continue

    if (nr, nc) == bomb_coordinates:
        game_map[nr][nc] = "B"
    else:
        game_map[nr][nc] = "*"

    nr, nc = nr + dr, nc + dc

    if game_map[nr][nc] == "T":
        game_map[nr][nc] = "*"
        print("Terrorists win!")
        break

    game_map[nr][nc] = "C"

game_map[player_coordinates[0]][player_coordinates[1]] = "C"

for line in game_map:
    print(*line, sep="")