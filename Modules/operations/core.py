mapper = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: y - x,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y,
}

def calculate(num1: float, num2: float, sign: str) -> float:
    try:
        result = mapper[sign](num1, num2)
    except KeyError:
        result = None

    return result