import math

number: int = int(input())
log_base: str = input()
try:
    result: float = math.log(number, int(log_base))
except ValueError:
    result: float = math.log(number)

print(f"{result:.2f}")