rows: int = int(input())

matrix: list[list[int]] = [list(map(int, input().split(", "))) for _ in range(rows)]

primary_diagonal: list[int] = [matrix[r][r] for r in range(rows)]
secondary_diagonal: list[int] = [matrix[r][-1 - r] for r in range(rows)]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")