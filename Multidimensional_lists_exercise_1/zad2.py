rows: int = int(input())

matrix: list[list[int]] = [list(map(int, input().split())) for _ in range(rows)]

primary_diagonal_sum: int = sum(matrix[r][r] for r in range(rows))
secondary_diagonal_sum: int = sum(matrix[r][rows - r - 1] for r in range(rows))

print(abs(primary_diagonal_sum - secondary_diagonal_sum))