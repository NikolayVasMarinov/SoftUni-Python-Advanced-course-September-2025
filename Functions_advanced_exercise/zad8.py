def age_assignment(*args: str, **kwargs: int) -> str:
    names_dict: dict[str, int] = {
        name: kwargs[name[0]]
        for name in args
    }

    names_dict = dict(sorted(names_dict.items(), key=lambda x: x[0]))

    result: list[str] = [f"{name} is {age} years old." for name, age in names_dict.items()]

    return "\n".join(result)