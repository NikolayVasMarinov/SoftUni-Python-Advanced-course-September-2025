def even_odd_filter(**kwargs) -> dict[str, list[int]]:
    result: dict[str, list[int]] = {}

    for key, numbers in kwargs.items():
        if key == "even":
            result[key] = [n for n in numbers if n % 2 == 0]
        elif key == "odd":
            result[key] = [n for n in numbers if n % 2 != 0]

    return dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))
