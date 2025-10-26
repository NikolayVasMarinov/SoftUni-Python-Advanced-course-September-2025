Coordinate = tuple[int, int]

shotgun_range: list[list[str]] = [list(input().split()) for _ in range(5)]

position: Coordinate = next((row, col) for row in range(5)
                            for col in range(5)
                            if shotgun_range[row][col] == "A")

target_amount: int = len([(row, col) for row in range(5)
                            for col in range(5)
                            if shotgun_range[row][col] == "x"])

directions: dict[str, Coordinate] = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
}

targets_shot: list[list[int]] = []

for _ in range(int(input())):
    command: list[str] = input().split()
    action: str = command[0]
    direction: str = command[1]
    dr, dc = directions[direction]

    if action == "move":
        steps = int(command[2])
        r, c = position[0] + dr * steps, position[1] + dc * steps

        if 0 <= r < 5 and 0 <= c < 5 and shotgun_range[r][c] == ".":
            shotgun_range[position[0]][position[1]] = "."
            shotgun_range[r][c] = "A"
            position = r, c

    elif action == "shoot":
        r, c = position

        while True:
            r, c = r + dr, c + dc

            if not (0 <= r < 5 and 0 <= c < 5):
                break

            if shotgun_range[r][c] == "x":
                shotgun_range[r][c] = "."
                targets_shot.append([r, c])
                target_amount -= 1
                break

    if target_amount == 0:
        print(f"Training completed! All {len(targets_shot)} targets hit.")
        break

else:
    print(f"Training not completed! {target_amount} targets left.")

if targets_shot:
    print(*targets_shot, sep="\n")
