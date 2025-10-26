Coordinate = tuple[int, int]

size: int = int(input())
territory: list[list[str]] = [list(input().split()) for _ in range(size)]

alice_position: Coordinate = next((row, col) for row in range(len(territory))
                                        for col in range(len(territory[0]))
                                        if territory[row][col] == "A")

tea_amount: int = 0

directions: dict[str, Coordinate] = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
}

territory[alice_position[0]][alice_position[1]] = "*"

while tea_amount < 10:
    direction = input()
    nr, nc = alice_position[0] + directions[direction][0], alice_position[1] + directions[direction][1]

    if not (0 <= nr < size and 0 <= nc < size):
        print("Alice didn't make it to the tea party.")
        break

    if territory[nr][nc] == "R":
        territory[nr][nc] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if territory[nr][nc].isdigit():
        tea_amount += int(territory[nr][nc])

    territory[nr][nc] = "*"
    alice_position = nr, nc

else:
    print("She did it! She went to the party.")

for row in territory:
    print(*row)