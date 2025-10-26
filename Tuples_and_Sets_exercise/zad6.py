odd_numbers: set[int] = set()
even_numbers: set[int] = set()

for row in range(1, int(input()) + 1):
    name: str = input()

    ascii_sum: int = sum(ord(ch) for ch in name) // row

    if ascii_sum % 2 == 0:
        even_numbers.add(ascii_sum)
    else:
        odd_numbers.add(ascii_sum)

odd_sum: int = sum(odd_numbers)
even_sum: int = sum(even_numbers)

if odd_sum == even_sum:
    print(*odd_numbers.union(even_numbers), sep= ", ")
elif odd_sum > even_sum:
    print(*odd_numbers.difference(even_numbers), sep= ", ")
else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep= ", ")