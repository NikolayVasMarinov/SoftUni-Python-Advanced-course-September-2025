from collections import deque
from typing import Deque

def turn_starting_time_to_seconds() -> int:
    hours, minutes, seconds = map(int, input().split(":"))

    starting_time_in_seconds = hours * 3600 + minutes * 60 + seconds

    return starting_time_in_seconds

def format_time(time_in_seconds: int) -> str:
    hours: int = (time_in_seconds // 3600) % 24
    minutes: int = (time_in_seconds % 3600) // 60
    seconds: int = time_in_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def tick_robots(robots_in_use: dict[str, tuple[int, int]]) -> None:
    for robot, (process_time, time_left) in robots_in_use.items():
        if time_left > 0:
            robots_in_use[robot] = (process_time, time_left - 1)

def assign_robot(robots_in_use: dict[str, tuple[int, int]], products_queued: Deque[str],
                 processed_product: str, time: int) -> None:

    for robot, (process_time, time_left) in robots_in_use.items():
        if time_left <= 0:
            robots_in_use[robot] = (process_time, process_time)

            print(f"{robot} - {processed_product} [{format_time(time)}]")
            break

        robots_in_use[robot] = (process_time, time_left)

    else:
        products_queued.append(processed_product)

robots_information: list[str] = input().split(";")

robots: dict[str, tuple[int, int]] = {robot_name: (int(robot_processing_time), 0)
                                      for robot_name, robot_processing_time
                                      in (r.split("-") for r in robots_information)}

current_time: int = turn_starting_time_to_seconds()
queued_products: Deque[str] = deque()

while (product:= input()) != "End":
    queued_products.append(product)

while queued_products:
    current_time += 1
    tick_robots(robots)

    product: str = queued_products.popleft()
    assign_robot(robots, queued_products, product, current_time)