import re

with open("words.txt") as file:
    words: dict[str, int] = {word: 0 for word in file.read().split()}

with open("text.txt") as file:
    text: str = file.read()

for word in words.keys():
    words[word] = len(re.findall(f"\\b{word}\\b", text, re.IGNORECASE))

words = dict(sorted(words.items(), key= lambda x: -x[1]))

with open("output.txt", "w") as file:
    for word, count in words.items():
        file.write(f"{word} - {count}\n")