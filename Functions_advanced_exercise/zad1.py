def sum_numbers(*args: list[int]) -> tuple[int, int]:
    return sum(x for x in args if x > 0), sum(x for x in args if x < 0)

numbers = [int(x) for x in input().split()]

positive_numbers_sum, negative_numbers_sum = sum_numbers(*numbers)


print(negative_numbers_sum)
print(positive_numbers_sum)
if positive_numbers_sum < abs(negative_numbers_sum):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")