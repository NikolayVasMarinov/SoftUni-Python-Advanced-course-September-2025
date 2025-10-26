def concatenate(*args: list[str], **kwargs: dict[str, str]) -> str:
    result: str = "".join(args)

    for key, text in kwargs.items():
        if key in result:
            result = result.replace(key, text)

    return result