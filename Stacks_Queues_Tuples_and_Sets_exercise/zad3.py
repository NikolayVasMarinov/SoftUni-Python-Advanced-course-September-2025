from collections import deque
from typing import Deque

chocolates: list[int] = list(map(int, input().split(", ")))
cups_of_milk: Deque[int] = deque(map(int, input().split(", ")))
milkshakes: int = 0

while chocolates and cups_of_milk and milkshakes < 5:
    chocolate: int = chocolates.pop()
    current_cup: int = cups_of_milk.popleft()

    if chocolate <= 0 or current_cup <= 0:
        if chocolate > 0:
            chocolates.append(chocolate)
            
        elif current_cup > 0:
            cups_of_milk.appendleft(current_cup)

        continue

    if current_cup == chocolate:
        milkshakes += 1

    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(current_cup)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")

else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, cups_of_milk)) if cups_of_milk else 'empty'}")