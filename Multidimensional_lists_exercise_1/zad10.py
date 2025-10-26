from typing import Callable
def parse_input() -> tuple[int, int, list[list[str]], list[str]]:
    r, c = map(int, input().split())
    grid = [list(input()) for _ in range(r)]
    movements = list(input())

    return r, c, grid, movements

def get_symbol_coordinates(grid: list[list[str]], symbol: str) -> list[tuple[int, int]]:
    return [(row, col)
            for row in range(len(grid))
            for col in range(len(grid[0]))
            if grid[row][col] == symbol]

def spread__bunnies(grid: list[list[str]], bunny_positions: set[tuple[int, int]]) -> set[tuple[int, int]]:
    new_bunnies = set(bunny_positions)

    for r, c in bunny_positions:
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                grid[nr][nc] = "B"
                new_bunnies.add((nr, nc))

    return new_bunnies

rows, columns, lair, player_movement = parse_input()
won: bool = False
died: bool = False

player_position: tuple[int, int] = get_symbol_coordinates(lair, "P")[0]

bunnies: set[tuple[int, int]] = set(get_symbol_coordinates(lair, "B"))

moves: dict[str, Callable[[int, int], tuple[int, int]]] = {
    "U":  lambda r, c: (r - 1, c),
    "D":  lambda r, c: (r + 1, c),
    "L":  lambda r, c: (r, c - 1),
    "R":  lambda r, c: (r, c + 1),
}
end_coordinates: tuple[int, ...] = tuple()

for direction in player_movement:
    new_row, new_column = moves[direction](player_position[0], player_position[1])
    new_lair = [row[:] for row in lair]
    new_lair[player_position[0]][player_position[1]] = "."

    if not (0 <= new_row < rows and 0 <= new_column < columns):
        end_coordinates = (player_position[0], player_position[1])
        lair[player_position[0]][player_position[1]] = "."
        won = True

    elif (new_row, new_column) in bunnies:
        end_coordinates = (new_row, new_column)
        died = True

    else:
        new_lair[new_row][new_column] = "P"
        player_position = (new_row, new_column)

    bunnies = spread__bunnies(new_lair, bunnies)
    lair = new_lair

    if (new_row, new_column) in bunnies:
        end_coordinates = (new_row, new_column)
        died = True

    if won or died:
        break

for r in lair:
    print(*r, sep= "")

if won: print("won: ", end= "")
elif died: print("dead: ", end= "")
print(f"{end_coordinates[0]} {end_coordinates[1]}")