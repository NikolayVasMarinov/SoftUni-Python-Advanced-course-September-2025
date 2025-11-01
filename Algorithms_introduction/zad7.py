def selection_sort(nums: list[int]) -> None:
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


numbers: list[int] = list(map(int, input().split()))

selection_sort(numbers)

print(*numbers)