from Modules.operations.core import calculate

num1, sign, num2 = input().split()
num1 = float(num1)
num2 = float(num2)

print(f"{calculate(num1, num2, sign):.2f}")