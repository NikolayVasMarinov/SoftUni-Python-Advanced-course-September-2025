def grocery_store(**kwargs: dict[str, int]):
    kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = ""

    for key, value in kwargs.items():
        result += f"{key}: {value}\n"

    return result