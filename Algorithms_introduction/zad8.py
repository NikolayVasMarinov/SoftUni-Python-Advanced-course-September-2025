def bubble_sort(nums: list[int]) -> None:
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


numbers: list[int] = list(map(int, input().split()))

bubble_sort(numbers)

print(" ".join(map(str, numbers)))