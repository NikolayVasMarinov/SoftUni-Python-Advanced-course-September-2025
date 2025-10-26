number_of_usernames: int = int(input())

unique_usernames: set[str] = set(input() for _ in range(number_of_usernames))

print(*unique_usernames, sep= "\n")