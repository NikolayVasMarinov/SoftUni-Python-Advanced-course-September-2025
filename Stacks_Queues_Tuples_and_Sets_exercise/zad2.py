from collections import deque
from typing import Deque
from math import prod

expression: list[str] = input().split(" ")
saved_characters: Deque[int] = deque()

for character in expression:
    if character.lstrip("-").isdigit():
        saved_characters.append(int(character))

    match character:
        case "+":
            saved_characters = deque([sum(saved_characters)])

        case "-":
            saved_characters = deque([saved_characters.popleft() - sum(saved_characters)])

        case "*":
            saved_characters = deque([prod(saved_characters)])

        case "/":
            result: int = saved_characters.popleft()

            while saved_characters:
                result //= saved_characters.pop()

            saved_characters.append(result)

print(saved_characters[0])