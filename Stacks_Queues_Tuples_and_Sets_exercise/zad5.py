from collections import deque
from typing import Deque

material_boxes: Deque[int] = deque(map(int, input().split()))
magic_values: Deque[int] = deque(map(int, input().split()))
presents: list[str] = []

magic_needed: dict[int, str] = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while material_boxes and magic_values:
    material: int = material_boxes.pop()
    magic: int = magic_values.popleft()

    if magic == 0 or material == 0:
        if magic != 0:
            magic_values.appendleft(magic)

        elif material != 0:
            material_boxes.append(material)

        continue

    magic_value: int = magic * material

    if magic_needed.get(magic_value):
        presents.append(magic_needed[magic_value])

    elif magic_value < 0:
        material_boxes.append(magic + material)


    else:
        material_boxes.append(material + 15)


if (("Doll" in presents and "Wooden train" in presents)
        or ("Teddy bear" in presents and "Bicycle" in presents)):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if material_boxes:
    print(f"Materials left: {', '.join(map(str, deque(reversed(material_boxes))))}")
if magic_values:
    print(f"Magic left: {', '.join(map(str, magic_values))}")

for present in sorted(set(presents)):
    print(f"{present}: {presents.count(present)}")
