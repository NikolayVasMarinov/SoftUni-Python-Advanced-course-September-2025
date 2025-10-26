number_of_commands: int = int(input())
parked_cars: set[str] = set()

for _ in range(number_of_commands):
    direction: str
    car_number: str
    direction, car_number = input().split(", ")

    match direction:
        case "IN":
            parked_cars.add(car_number)
        case "OUT":
            parked_cars.remove(car_number)

if parked_cars:
    print(*parked_cars, sep="\n")
else:
    print("Parking Lot is Empty")