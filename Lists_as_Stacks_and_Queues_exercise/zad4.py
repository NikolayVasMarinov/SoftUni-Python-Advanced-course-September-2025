box_of_clothes: list[int] = [int(x) for x in input().split(" ")]
one_rack_capacity: int = int(input())
racks_needed_for_clothes: int = 0

while box_of_clothes:
    racks_needed_for_clothes += 1
    current_rack_capacity: int = one_rack_capacity

    while box_of_clothes and current_rack_capacity < one_rack_capacity:
        current_rack_capacity -= box_of_clothes.pop()

print(racks_needed_for_clothes)