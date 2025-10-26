number_of_intersections: int = int(input())
biggest_intersection: list[int] = []

for _ in range(number_of_intersections):
    first_range: str
    second_range: str
    first_range, second_range = input().split("-")

    first_start: int
    first_end: int
    second_start: int
    second_end: int

    first_start, first_end = map(int, first_range.split(","))
    second_start, second_end = map(int, second_range.split(","))

    first_set: set[int] = set(range(first_start, first_end + 1))
    second_set: set[int] = set(range(second_start, second_end + 1))

    intersection: list[int] = sorted((first_set.intersection(second_set)))

    if len(intersection) > len(biggest_intersection):
        biggest_intersection = intersection

print(f"Longest intersection is {biggest_intersection} with length {len(biggest_intersection)}")
