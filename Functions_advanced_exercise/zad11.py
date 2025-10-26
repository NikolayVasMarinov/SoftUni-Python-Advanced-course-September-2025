def math_operations(*args: float, **kwargs: float) -> str:
    result = ""

    for i, num in enumerate(args):
        key = list(kwargs.keys())[i % len(kwargs)]

        if key == "a":
            kwargs[key] += num

        elif key == "s":
            kwargs[key] -= num

        elif key == "d":
            if num != 0:
                kwargs[key] /= num

        elif key == "m":
            kwargs[key] *= num

    kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))

    for key, value in kwargs.items():
        result += f"{key}: {value:.1f}\n"

    return result