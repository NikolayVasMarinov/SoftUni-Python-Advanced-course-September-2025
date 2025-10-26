numbers: tuple = tuple(map(float, input().split(" ")))

occurrences: dict[float, int] = {}
for number in numbers:
    if number not in occurrences:
        occurrences[number] = 0

    occurrences[number] += 1

[print(f"{key} - {value} times") for key, value in occurrences.items()]