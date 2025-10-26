matrix: list[int] = [int(x) for row in input().split("|")[::-1] for x in row.split() ]

print(*matrix)