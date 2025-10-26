from collections import deque
from typing import Deque, Callable

bees: Deque[int] = deque(map(int, input().split()))
nectar: Deque[int] = deque(map(int, input().split()))
symbols: Deque[str] = deque(input().split())
total_honey: int = 0

operations: dict[str, Callable[[int, int], int]] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: abs(a - b),
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while bees and nectar:
    current_nectar: int = nectar.pop()

    if current_nectar < bees[0]:
        continue

    else:
        bee: int = bees.popleft()
        symbol: str = symbols.popleft()

        total_honey += operations[symbol](bee, current_nectar)


print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}" )