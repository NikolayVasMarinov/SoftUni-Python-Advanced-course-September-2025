from collections import deque
from typing import Deque

POTIONS = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90:  "Draught of Wisdom",
    80:  "Potion of Agility",
    70:  "Elixir of Strength"
}

substances: list[int] = [int(x) for x in input().split(", ")]
crystals: Deque[int] = deque(int(x) for x in input().split(", "))

crafted_potions: list[str] = []

while substances and crystals:
    substance = substances.pop()
    crystal = crystals.popleft()

    energy = substance + crystal

    if POTIONS.get(energy) and POTIONS[energy] not in crafted_potions:
        crafted_potions.append(POTIONS[energy])

    elif energy > 70:
        for energy_needed in POTIONS.keys():
            if energy_needed < energy and POTIONS[energy_needed] not in crafted_potions:
                crafted_potions.append(POTIONS[energy_needed])
                break

        if crystal - 20 > 0:
            crystals.append(crystal - 20)

    else:
        if crystal - 5 > 0:
            crystals.append(crystal - 5)

    if len(crafted_potions) == 5:
        print("Success! The alchemist has forged all potions!")
        break

else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print("Crafted potions: ", end="")
    print(*crafted_potions, sep=", ")

if substances:
    print("Substances: ", end="")
    print(*substances[::-1], sep=", ")
if crystals:
    print("Crystals: ", end="")
    print(*crystals, sep=", ")