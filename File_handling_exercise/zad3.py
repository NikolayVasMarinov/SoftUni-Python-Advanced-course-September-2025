import os

while (command := input()) != "End":
    command_parts = command.split("-")
    action, file_name = command_parts[:2]

    if action == "Create":
        with open(file_name, "w") as f:
            pass

    elif action == "Add":
        content = command_parts[2]
        with open(file_name, "a") as f:

            f.write(f"{content}\n")

    elif action == "Replace":
        if not os.path.exists(file_name):
            print("An error occurred")
            continue

        old_content = command_parts[2]
        new_content = command_parts[3]

        with open(file_name, "r+") as f:
            text = f.read()
            text = text.replace(old_content, new_content)
            f.seek(0)
            f.write(text)
            f.truncate()

    elif action == "Delete":
        if not os.path.exists(file_name):
            print("An error occurred")
            continue

        os.remove(file_name)