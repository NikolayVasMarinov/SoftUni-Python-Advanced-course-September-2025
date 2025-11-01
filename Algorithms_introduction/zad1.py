def calculate_sum(numbers: list[int], i: int) -> int:
    if i >= len(numbers): return 0

    return numbers[i] +calculate_sum(numbers, i + 1)

nums = list(map(int, input().split()))

print(calculate_sum(nums, 0))