from collections import deque

def fill_the_box(height: int, length: int, width: int, *args: [int, str]) -> str:
    volume: int = height * length * width
    args = deque(args)

    while args:
        number = args.popleft()
        if number == "Finish":
            return f"There is free space in the box. You could put {volume} more cubes."

        volume -= number

        if volume <= 0:
            free_space_left: int = -volume + sum(x for x in args if x != "Finish")
            return f"No more free space! You have {free_space_left} more cubes."