def create_sequence(n: int) -> None:
    num1 = 0
    num2 = 1

    if n == 1: print(num1)
    if n >= 2: print(num1, num2, end= " ")

    n -= 2

    while n > 0:
        temp = num1
        num1 = num2
        num2 += temp
        print(num2, end= " ")

        n -= 1

    print()

def locate(n: int) -> None:
    num1 = 0
    num2 = 1

    if n == 0: result = 0
    if n == 1: result = 1

    i = 2

    while True:
        temp = num1
        num1 = num2
        num2 += temp

        if num2 == n:
            result = i
            break

        if num2 > n:
            result = None
            break

        i += 1


    if result:
        print(f"The number - {n} is at index {result}")
    else:
        print(f"The number {n} is not in the sequence")
