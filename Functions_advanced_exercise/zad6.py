from typing import Callable, Any

def func_executor(*args: tuple[Callable[..., Any], tuple[Any, ...]]) -> str:
    result:str = ""

    for func, arguments in args:
        result += f"{func.__name__} - {func(*arguments)}\n"

    return result