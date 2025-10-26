def print_triangle(size: int) -> None:
    for i in range(1, size + 1):
        print(*range(1, i + 1))

    for i in range(size - 1, 0, -1):
        print(*range(1, i + 1))