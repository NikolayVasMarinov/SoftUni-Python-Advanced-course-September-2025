expression = list(input())
stack: list[int] = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)

    elif expression[index] == ")":
        opening_parenthesis_index: int = stack.pop()
        parenthesis: str = "".join(expression[opening_parenthesis_index:index + 1])

        print(parenthesis)