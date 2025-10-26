rows: int
columns: int
rows, columns = map(int, input().split(", "))

matrix: list[list[int]] = [list(map(int, input().split())) for _ in range(rows)]

for column in zip(*matrix):
    print(sum(column))