Coordinate = tuple[int, ...]

presents_amount: int = int(input())
size: int = int(input())
neighbourhood: list[list[str]] = []
santa_position: Coordinate = tuple()
nice_kids_amount: int = 0


for r in range(size):
    neighbourhood.append(list(input().split()))
    for c in range(size):
        if neighbourhood[r][c] == "S":
            santa_position = (r, c)

        elif neighbourhood[r][c] == "V":
            nice_kids_amount += 1

nice_kids_left: int = nice_kids_amount

directions: dict[str, Coordinate] = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
}

while (command := input()) != "Christmas morning":
    dr, dc = directions[command]

    nr, nc = santa_position[0] + dr, santa_position[1] + dc

    if neighbourhood[nr][nc] == "V":
        nice_kids_left -= 1
        presents_amount -= 1

    elif neighbourhood[nr][nc] == "C":

        for r, c in [(nr - 1, nc), (nr + 1, nc), (nr, nc - 1), (nr, nc + 1)]:
            if neighbourhood[r][c] == "X":
                neighbourhood[r][c] = "-"
                presents_amount -= 1

            elif neighbourhood[r][c] == "V":
                neighbourhood[r][c] = "-"
                presents_amount -= 1
                nice_kids_left -= 1

            if presents_amount == 0:

                break

            if nice_kids_left == 0:
                break

    neighbourhood[santa_position[0]][santa_position[1]] = "-"
    neighbourhood[nr][nc] = "S"
    santa_position = nr, nc

    if nice_kids_left == 0:
        break

    if presents_amount == 0:
        print("Santa ran out of presents!")
        break

for row in neighbourhood:
    print(*row)

if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids_amount} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")

