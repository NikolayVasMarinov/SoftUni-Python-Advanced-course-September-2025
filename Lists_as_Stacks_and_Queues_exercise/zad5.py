from collections import deque
from typing import Deque

number_of_petrol_pumps: int = int(input())
petrol_pumps: Deque[dict] = deque()

for pump in range(number_of_petrol_pumps):
    petrol_pump = input().split()

    petrol_pumps.append({"petrol amount": int(petrol_pump[0]), "distance": int(petrol_pump[1])})

fuel_amount: int = 0
pumps_visited: int = 0
times_rotated: int = 0

while pumps_visited < number_of_petrol_pumps:
    fuel_amount += petrol_pumps[0]["petrol amount"] - petrol_pumps[0]["distance"]
    pumps_visited += 1

    if fuel_amount < 0:
        pumps_visited = 0
        fuel_amount = 0

    petrol_pumps.rotate(-1)
    times_rotated += 1


print(times_rotated - len(petrol_pumps))
