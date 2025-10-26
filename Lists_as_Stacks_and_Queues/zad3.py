from collections import deque

customers: deque[str] = deque()

while (command := input()) != "End":
    if command == "Paid":
        while customers:
            print(customers.popleft())

        continue

    customer_name: str = command

    customers.append(customer_name)

print(f"{len(customers)} people remaining.")