from collections import deque
from typing import Deque

cups: Deque[int] = deque(map(int, input().split(" ")))
filled_bottles: Deque[int] = deque(map(int, input().split(" ")))
wasted_liters_water: int = 0

while cups:
    if not filled_bottles:
        break

    bottle: int = filled_bottles.pop()

    cup: int  = cups[0]
    leftover_water: int = bottle - cup

    if leftover_water >= 0:
        wasted_liters_water += leftover_water
        cups.popleft()

    else:
        cups[0] -= bottle

if cups:
    print(f"Cups: ", *cups)
else:
    print(f"Bottles: ", *filled_bottles)

print(f"Wasted litters of water: {wasted_liters_water}")