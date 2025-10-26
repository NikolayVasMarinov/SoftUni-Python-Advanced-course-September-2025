rows: int
columns: int
rows, columns = map(int, input().split(", "))

matrix: list[list[int]] = [list(map(int, input().split(", "))) for _ in range(rows)]
max_sum: int = 0
max_submatrix: list[list[int]] = []

for r in range(rows - 1):
    for c in range(columns - 1):

        current_submatrix = [
            [matrix[r][c], matrix[r][c + 1]],
            [matrix[r + 1][c], matrix[r + 1][c + 1]]
        ]

        current_sum = sum(sum(row) for row in current_submatrix)

        if current_sum > max_sum:
            max_sum = current_sum
            max_submatrix = current_submatrix

for row in max_submatrix:
    print(*row, sep=" ")

print(max_sum)