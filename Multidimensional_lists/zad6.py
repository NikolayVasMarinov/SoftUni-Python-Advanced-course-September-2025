matrix_size: int = int(input())

matrix: list[list[str]] = [list(input()) for _ in range(matrix_size)]

symbol: str = input()

position = next(((r, c) for r in range(matrix_size)
                 for c in range(matrix_size) if matrix[r][c] == symbol), None)

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")