from pyfiglet import figlet_format

text: str = input()

text = figlet_format(text)
print(text)