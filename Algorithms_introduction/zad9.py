def insertion_sort(nums: list[int]) -> None:
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1


numbers: list[int] = list(map(int, input().split()))

insertion_sort(numbers)

print(*numbers)