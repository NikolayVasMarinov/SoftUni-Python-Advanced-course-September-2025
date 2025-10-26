file = open("numbers.txt")

sum_numbers: int = sum(map(int, file.read().split("\n")))

print(sum_numbers)

file.close()