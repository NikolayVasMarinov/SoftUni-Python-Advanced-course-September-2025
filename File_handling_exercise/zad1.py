SPECIAL_CHARACTERS = {"-", ",", ".", "!", "?"}

with open("text.txt") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            for ch in SPECIAL_CHARACTERS:
                line = line.replace(ch, "@")

            print(" ".join(line.split()[::-1]))
