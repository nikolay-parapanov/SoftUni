from collections import deque

quantity = int(input())

orders = deque(int(x) for x in input().split())
total_orders = len(orders)

flag = True
print(max(orders))

for i in range(total_orders):
    current_order = orders.popleft()
    if quantity >= current_order:
        quantity -= current_order
    else:
        orders.appendleft(current_order)
        flag = False
        break

if flag:
    print("Orders complete")
else:
    orders_str = [str(x) for x in orders]
    print(f'Orders left:'," ".join(orders_str))

