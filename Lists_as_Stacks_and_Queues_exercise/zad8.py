from collections import deque
from typing import Deque

def green_light_cycle(queued_cars: Deque[str], green_light_duration_left: int,
                      free_window_duration_left: int) -> tuple[int, bool]:
    crash_happened = False
    cars_passed = 0

    while green_light_duration_left > 0 and queued_cars:
        car_name: str = queued_cars.popleft()
        passing_car: Deque[str]  = deque(car_name)

        while passing_car:
            if green_light_duration_left == 0:
                if tick_free_window(passing_car, free_window_duration_left, car_name):
                    crash_happened = True
                else:
                    cars_passed += 1

                break

            green_light_duration_left -= 1
            passing_car.popleft()
        else:
            cars_passed += 1
    return cars_passed, crash_happened

def tick_free_window(passing_car: Deque[str], free_window_duration_left: int, car_name: str) -> bool:
    crash_happened = False

    while passing_car:
        if free_window_duration_left == 0:
            print(f"A crash happened!\n{car_name} was hit at {passing_car.popleft()}.")
            crash_happened = True
            break

        free_window_duration_left -= 1
        passing_car.popleft()

    return crash_happened

green_light_duration: int = int(input())
free_window_duration: int = int(input())
cars_queued: Deque[str] = deque()
total_cars_passed = 0
crash_detected = False

while (command:= input()) != "END":
    match command:
        case "green":
            passed, crash_detected = green_light_cycle(cars_queued, green_light_duration,
                                               free_window_duration)
            total_cars_passed += passed

        case _:
            cars_queued.append(command)

    if crash_detected:
        break
else:
    print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")