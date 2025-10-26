coordinate = tuple[int, int]

def valid(r: int, c: int, board_size: int) -> bool:
    return 0 <= r < board_size and 0 <= c < board_size

def count_attacks(r: int, c: int, brd: list[list[str]], board_size: int) -> int:
    cnt = 0

    for dr, dc in knight_offsets:
        nr, nc = r + dr, c + dc
        if valid(nr, nc, board_size) and brd[nr][nc] == "K":
            cnt += 1

    return cnt

size: int = int(input())

board: list[list[str]] = [list(input()) for _ in range(size)]

knight_coordinates = [(r, c) for r in range(size)
                      for c in range(size)
                      if board[r][c] == "K"]

knights_removed: int = 0

knight_offsets: list[coordinate] = [
        (-2, -1), (-2, +1),
        (-1, +2), (+1, +2),
        (+2, +1), (+2, -1),
        (+1, -2), (-1, -2),
    ]

while True:
    best_coordinate: tuple[int, int] = (0, 0)
    max_len: int = 0
    for row, col in knight_coordinates:
        possible_attacks: int = count_attacks(row, col, board, size)

        if possible_attacks > max_len:
            max_len = possible_attacks
            best_coordinate = (row, col)

    if max_len == 0:
        break

    board[best_coordinate[0]][best_coordinate[1]] = "0"
    knight_coordinates.remove((best_coordinate[0], best_coordinate[1]))
    knights_removed += 1

print(knights_removed)