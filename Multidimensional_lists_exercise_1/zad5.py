rows: int
columns: int
rows, columns = map(int, input().split())

matrix: list[list[str]] = [
    [chr(r + 97) + chr(r + c + 97) + chr(r + 97) for c in range(columns)]
    for r in range(rows)
]

for row in matrix:
    print(*row)