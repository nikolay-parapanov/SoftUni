from collections import deque

ramen = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))


while ramen and customers:
    current_ramen = ramen.pop()
    current_customer = customers.popleft()

    if current_customer > current_ramen:
        current_customer -= current_ramen
        customers.appendleft(current_customer)
    elif current_customer < current_ramen:
        current_ramen -= current_customer
        ramen.append(current_ramen)

ramen_str = ', '.join(str(x) for x in ramen)
customers_str = ', '.join(str(x) for x in customers)

if not customers:
    print(f"Great job! You served all the customers.")
    if ramen:
        print(f'Bowls of ramen left: {ramen_str}')
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {customers_str}')
