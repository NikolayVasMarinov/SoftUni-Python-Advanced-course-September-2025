numbers: set[int] = set(map(int, input().split(" ")))
target_number:int = int(input())
seen_numbers: set[int] = set()

for number in numbers:
    complement: int = target_number - number

    if complement in seen_numbers:
        print(f"{complement} + {number} = {target_number}")

    seen_numbers.add(number)