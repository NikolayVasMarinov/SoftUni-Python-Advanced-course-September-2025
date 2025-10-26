rows: int = int(input())

matrix: list[list[int]] = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)]

print(matrix)

