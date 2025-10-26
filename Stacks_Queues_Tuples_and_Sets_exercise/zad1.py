first_sequence: set[int] = set(map(int, input().split(" ")))
second_sequence: set[int] = set(map(int, input().split(" ")))

for _ in range(int(input())):
    command: list[str] = input().split(" ")
    action: str
    sequence: list[int]
    action, sequence = " ".join(command[:2]), list(map(int, command[2:]))

    match action:
        case "Add First":
            first_sequence.update(sequence)

        case "Add Second":
            second_sequence.update(sequence)

        case "Remove First":
            first_sequence.difference_update(sequence)

        case "Remove Second":
            second_sequence.difference_update(sequence)

        case "Check Subset":
            if first_sequence > second_sequence or first_sequence < second_sequence:
                print(True)

            else:
                print(False)

print(*sorted(first_sequence), sep= ", ")
print(*sorted(second_sequence), sep= ", ")