text = list(input())
stack: list[str] = []

for index in range(len(text)):
    stack.append(text.pop())

print("".join(stack))
