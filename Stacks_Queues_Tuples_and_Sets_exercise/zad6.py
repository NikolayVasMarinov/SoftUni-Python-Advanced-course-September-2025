from collections import deque
from typing import Deque

substrings: Deque[str] = deque(input().split())
colors: tuple[str, ...] = ("red", "blue", "yellow", "orange", "purple", "green")
found_colors: list[str] = []
dependencies: dict[str, tuple[str, str]] = {
    "orange": ("yellow", "red"),
    "purple": ("blue", "red"),
    "green": ("yellow", "blue"),
}

while len(substrings) > 1:
    first_substring: str = substrings.popleft()
    last_substring: str = substrings.pop()

    first_and_last_string: str = first_substring + last_substring
    last_and_first_string: str = last_substring + first_substring

    if first_and_last_string in colors:
        found_colors.append(first_and_last_string)

        continue

    if last_and_first_string in colors:
        found_colors.append(last_and_first_string)

        continue

    sliced_first: str = first_substring[:-1]
    sliced_last: str = last_substring[:-1]

    if sliced_last:
        substrings.insert(len(substrings) // 2, sliced_last)

    if sliced_first:
        substrings.insert(len(substrings) // 2, sliced_first)

if len(substrings) == 1 and substrings[0] in colors:
    found_colors.append(substrings[0])

filtered_colors: list[str] = []

for color in found_colors:
    if color in dependencies.keys():
        primary1, primary2 = dependencies[color]

        if not (primary1 in found_colors and primary2 in found_colors):
            continue

    filtered_colors.append(color)

print(filtered_colors)