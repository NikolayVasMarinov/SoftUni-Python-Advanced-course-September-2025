rows: int = int(input())

matrix: list[int] = [int(x) for _ in range(rows) for x in input().split(", ")]

print(matrix)