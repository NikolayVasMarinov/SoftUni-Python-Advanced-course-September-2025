from collections import deque
from typing import Deque

rows: int
columns: int
rows, columns = map(int, input().split())
snake: Deque[str] = deque(input())

matrix: list[list[str]] = []

for r in range(rows):
    matrix.append([])

    for _ in range(columns):
        matrix[r].append(snake[0])
        snake.rotate(-1)

for r, row in enumerate(matrix):
    if r % 2 == 1:
        print("".join(row[::-1]))

    else:
        print("".join(row))