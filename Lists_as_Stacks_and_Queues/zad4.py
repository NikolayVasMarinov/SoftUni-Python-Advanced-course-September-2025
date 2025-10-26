from collections import deque

def get_water(water_quantity: int, thirsty_person: str, taken_liters_water: int) -> int:
    if water_quantity - taken_liters_water < 0:
        print(f"{thirsty_person} must wait" )

        return water_quantity

    water_quantity -= taken_liters_water

    print(f"{thirsty_person} got water" )

    return water_quantity

def refill_water(water_quantity: int, liters_refilled: int) -> int:
    water_quantity += liters_refilled

    return water_quantity

water_quantity_liters: int = int(input())
thirsty_people: deque[str] = deque()

while (command := input()) != "Start":
    thirsty_person_name: str = command

    thirsty_people.append(thirsty_person_name)

while (command := input()) != "End":
    if command.startswith("refill "):
        liters: int = int(command.split(" ")[1])

        water_quantity_liters = refill_water(water_quantity_liters, liters)

        continue

    liters: int = int(command)

    water_quantity_liters = get_water(water_quantity_liters, thirsty_people.popleft(), liters)

print(f"{water_quantity_liters} liters left")