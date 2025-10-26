from Modules.fibonacci.core import create_sequence, locate

while (command := input()) != "Stop":
    command_parts = command.split()
    action = " ".join(command_parts[:-1])
    num: int = int(command_parts[-1])

    if action == "Create Sequence":
        create_sequence(num)

    elif action == "Locate":
        locate(num)