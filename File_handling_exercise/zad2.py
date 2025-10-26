import re

PUNCTUATION_CHARACTERS = {"-", ",", ".", "!", "?"}
with open("text.txt") as file, open("output.txt", "w") as f:
    for i, line in enumerate(file):
        f.write(f"Line {i + 1}: {line} "
                f"({len(re.findall(r'\w', line))})"
                f"""({len(re.findall(r"[-.,?!']", line))})\n""")