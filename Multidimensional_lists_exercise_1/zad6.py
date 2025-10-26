import re

rows: int
columns: int
rows, columns = map(int, input().split())

matrix: list[list[str]] = [input().split() for _ in range(rows)]

valid_command = r"swap(?: \d+){4}"

while (command:= input()) != "END":
    if not re.fullmatch(valid_command, command):
        print("Invalid input!")
        continue

    row1, column1, row2, column2 = map(int, command.split()[1:])

    coordinates = [(row1, column1), (row2, column2)]

    if not all(0 <= r < rows and 0 <= c < columns for r, c in coordinates):
        print("Invalid input!")
        continue

    matrix[row1][column1], matrix[row2][column2] = matrix[row2][column2], matrix[row1][column1]

    print("\n".join(" ".join(row) for row in matrix))