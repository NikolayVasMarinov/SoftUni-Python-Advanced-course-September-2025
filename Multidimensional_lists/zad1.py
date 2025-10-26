rows: int
columns: int
rows, columns = map(int, input().split(", "))
matrix: list[list[int]] = []
numbers_sum: int = 0

for _ in range(rows):
    row: list[int] = [int(x) for x in input().split(", ")]

    numbers_sum += sum(row)

    matrix.append(row)

print(numbers_sum)
print(matrix)