rows: int
columns: int
rows, columns = map(int, input().split())
max_sum: float = float("-inf")
max_square: list[list[int]] = []

matrix: list[list[int]] = [list(map(int, input().split())) for _ in range(rows)]

for r in range(rows - 2):
    for c in range(columns - 2):

        square = [
            matrix[r][c:c + 3],
            matrix[r + 1][c:c + 3],
            matrix[r + 2][c:c + 3]
        ]

        square_sum = sum(sum(row) for row in square)

        if square_sum > max_sum:
            max_sum = square_sum
            max_square = square

print(f"Sum = {max_sum}")
for row in max_square:
    print(*row)