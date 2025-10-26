from collections import deque

def operate(operator: str, *args) -> float:
    args = deque(args)

    def add(a) -> float:
        return sum(a)

    def subtract(a) -> float:
        result = a.popleft()

        while a:
            result -= a.popleft()

        return result

    def multiply(a) -> float:
        result = a.popleft()

        while a:
            result *= a.pop()

        return result

    def divide(a) -> float:
        result = a.popleft()

        while a:
            result /= a.popleft()

        return result

    match operator:
        case "+":
            return add(args)
        case "-":
            return subtract(args)
        case "*":
            return multiply(args)
        case "/":
            return divide(args)