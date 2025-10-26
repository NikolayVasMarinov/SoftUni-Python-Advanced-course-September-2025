first_set_length: int
second_set_length: int
first_set_length, second_set_length = map(int, input().split(" "))

first_set: set[int] = set(int(input()) for _ in range(first_set_length))
second_set: set[int] = set(int(input()) for _ in range(second_set_length))

print(*first_set.intersection(second_set), sep= "\n")
