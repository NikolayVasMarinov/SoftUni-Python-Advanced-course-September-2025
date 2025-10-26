def find_matches(field_size: int, field: list[list[str]], target: str) -> list[tuple[int, int]]:
    matches = [(r, c) for r in range(field_size)
               for c in range(field_size)
               if field[r][c] == target]

    return matches

def valid_coordinates(r: int, c: int, field_size: int) -> bool:
    return 0 <= r < field_size and 0 <= c < field_size

size: int = int(input())
miner_movement: list[str] = input().split()

mining_field: list[list[str]] = [input().split() for _ in range(size)]

miner_position: tuple[int, int] = find_matches(size, mining_field, "s")[0]
coal_amount: int = len(find_matches(size, mining_field, "c"))

moves: dict[str, tuple[int, int]] = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1),
}

for direction in miner_movement:
    row, column = moves[direction]

    new_row = miner_position[0] + row
    new_column = miner_position[1] + column

    if not valid_coordinates(new_row, new_column, size):
        continue

    miner_position = (new_row, new_column)

    match mining_field[new_row][new_column]:
        case "c":
            coal_amount -= 1
            mining_field[new_row][new_column] = "*"

            if coal_amount == 0:
                print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
                break
            
        case "e":
            print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
            break

else:
    print(f"{coal_amount} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")