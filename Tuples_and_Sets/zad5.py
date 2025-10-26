number_of_guests: int = int(input())
guests: set[str] = set()
guests_at_party: set[str] = set()

for guest in range(number_of_guests):
    guest_reservation_code: str = input()

    guests.add(guest_reservation_code)

while (command:= input()) != "END":
    guests.remove(command)

sorted_guests = sorted(guests)

print(len(sorted_guests), *sorted_guests, sep="\n")