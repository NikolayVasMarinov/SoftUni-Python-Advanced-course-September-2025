parenthesis_sequence: list[str] = list(input())
opening_brackets: list[str] = []

for character in parenthesis_sequence:
    match character:
        case "(":
            opening_brackets.append("(")

        case "{":
            opening_brackets.append("{")

        case "[":
            opening_brackets.append("[")

        case ")":
            if not opening_brackets:
                print("NO")
                break

            if opening_brackets.pop() !="(":
                print("NO")
                break

        case "}":
            if not opening_brackets:
                print("NO")
                break

            if opening_brackets.pop() != "{":
                print("NO")
                break

        case "]":
            if not opening_brackets:
                print("NO")
                break

            if opening_brackets.pop() != "[":
                print("NO")
                break
else:
    if opening_brackets:
        print("NO")

    else:
        print("YES")