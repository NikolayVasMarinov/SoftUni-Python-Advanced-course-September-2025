number_of_queries: int = int(input())
integer_stack: list[int] = []

for _ in range(number_of_queries):
    query: str = input()

    if not integer_stack:
        stack_is_empty = True
    else:
        stack_is_empty = False

    if query.startswith("1 "):
        number: int = int(query.split(" ")[1])

        integer_stack.append(number)

    elif not stack_is_empty:
        match query:
            case "2":
                integer_stack.pop()

            case "3":
                print(max(integer_stack))

            case "4":
                print(min(integer_stack))

print(*reversed(integer_stack), sep=", ")