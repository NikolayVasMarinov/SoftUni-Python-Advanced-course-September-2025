from collections import deque

food_quantity: int = int(input())
orders: deque[str] = deque(input().split(" "))

print(max(map(int, orders)))

while orders:
    order = int(orders[0])
    food_quantity -= order

    if food_quantity < 0:
        unfinished_orders = " ".join(orders)

        print(f"Orders left: {unfinished_orders}")
        break

    orders.popleft()

else:
    print("Orders complete")