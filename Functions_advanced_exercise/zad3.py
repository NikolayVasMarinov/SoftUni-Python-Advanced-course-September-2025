def even_odd(*args) -> list[int]:
    *numbers, command = args
    if command == "even":
        return [x for x in numbers if x % 2 == 0]

    elif command == "odd":
        return [x for x in numbers if x % 2 == 1]