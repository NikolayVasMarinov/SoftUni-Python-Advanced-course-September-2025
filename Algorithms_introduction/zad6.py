def find_index(nums: list[int], target) -> int:
    left_boundary: int = 0
    right_boundary: int = len(nums) - 1

    while right_boundary >= left_boundary:
        i: int = (left_boundary + right_boundary) // 2
        if target == nums[i]:
            return i

        elif target > nums[i]:
            left_boundary = i + 1

        else:
            right_boundary = i - 1

    return -1

numbers: list[int] = list(map(int, input().split()))
target_number: int = int(input())

print(find_index(numbers, target_number))