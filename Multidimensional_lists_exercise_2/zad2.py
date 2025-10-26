rows: int = int(input())
matrix: list[list[int]] = [[int(x) for x in input().split()] for _ in range(rows)]

while (command:= input()) != "END":
    action, row, column, value = command.split()
    row, column, value = map(int, (row, column, value))

    if not (0 <= row < rows and 0 <= column < len(matrix[0])):
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row][column] += value

    elif action == "Subtract":
        matrix[row][column] -= value

for row in matrix:
    print(*row)