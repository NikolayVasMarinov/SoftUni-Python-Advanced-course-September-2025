integers: list[str] = input().split(" ")
integer_stack = []

for index in range(len(integers)):
    integer_stack.append(integers.pop())

print(" ".join(integer_stack))
