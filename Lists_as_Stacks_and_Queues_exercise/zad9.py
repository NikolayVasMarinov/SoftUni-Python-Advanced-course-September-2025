from collections import deque
from typing import Deque

bullet_price: int = int(input())
gun_barrel_size: int = int(input())
bullets: Deque[int] = deque(map(int, input().split(" ")))
locks: Deque[int] = deque(map(int, input().split(" ")))
intelligence_value: int = int(input())
shots_fired: int = 0

while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break

    bullet: int = bullets.pop()
    shots_fired += 1

    if bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if shots_fired % gun_barrel_size == 0 and bullets:
        print("Reloading!")

else:
    profit: int = intelligence_value - shots_fired * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${profit}")