rows: int
columns: int
rows, columns = map(int, input().split())
count: int = 0

matrix: list[list[str]] = [input().split() for _ in range(rows)]

for r in range(rows - 1):
    for c in range(columns - 1):

        square_matrix = [
            matrix[r][c], matrix[r][c + 1],
            matrix[r + 1][c], matrix[r + 1][c + 1]
        ]

        if len(set(square_matrix)) == 1:
            count += 1

print(count)