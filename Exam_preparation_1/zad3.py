def list_roman_emperors(*args: tuple[str, bool], **kwargs: int) -> str:
    emperors: dict[str, bool] = {emperor: success for emperor, success in args}


    successful = {emperor: years for emperor, years in kwargs.items() if emperors[emperor]}
    unsuccessful = {emperor: years for emperor, years in kwargs.items() if not emperors[emperor]}

    sorted_emperors: dict[bool, dict[str, int]] = {
        True: dict(sorted(successful.items(), key= lambda x: (-x[1], x[0]))),
        False: dict(sorted(unsuccessful.items(), key= lambda x: (x[1], x[0])))
    }

    result_lines: list[str] = [f"Total number of emperors: {len(kwargs)}"]

    if sorted_emperors[True]:
        result_lines.append("Successful emperors:")
        result_lines.extend(f"****{name}: {years}" for name, years in sorted_emperors[True].items())

    if sorted_emperors[False]:
        result_lines.append("Unsuccessful emperors:")
        result_lines.extend(f"****{name}: {years}" for name, years in sorted_emperors[False].items())

    return "\n".join(result_lines)