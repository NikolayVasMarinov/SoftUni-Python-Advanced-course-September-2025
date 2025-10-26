def rectangle(a: int, b: int) -> str:
    if not type(a) == type(b) == int:
        return "Enter valid values!"

    return f"Rectangle area: {area(a, b)}\nRectangle perimeter: {perimeter(a, b)}"


def area(a: int, b: int) -> int:
    return a * b
def perimeter(a: int, b: int) -> int:
    return 2 * (a + b)