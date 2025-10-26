number_of_names: int = int(input())
unique_names: set[str] = set()

for _ in range(number_of_names):
    unique_names.add(input())

print(*unique_names, sep="\n")