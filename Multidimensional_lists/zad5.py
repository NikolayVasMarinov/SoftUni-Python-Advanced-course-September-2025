matrix_size: int = int(input())

matrix: list[list[int]] = [list(map(int, input().split())) for _ in range(matrix_size)]

main_diagonal_sum = sum(matrix[x][x] for x in range(matrix_size))

print(main_diagonal_sum)