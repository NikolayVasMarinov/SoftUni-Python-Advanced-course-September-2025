text: tuple[str] = tuple(input())

print(*sorted((f"{character}: {text.count(character)} time/s"
               for character in text)),
      sep= "\n")