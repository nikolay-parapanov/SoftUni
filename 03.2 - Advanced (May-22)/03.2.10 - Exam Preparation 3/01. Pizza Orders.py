from collections import deque

orders = deque(int(x) for x in input().split(', '))
employees = [int(x) for x in input().split(', ')]
total_pizzas = 0

while orders and employees:

    current_order = orders.popleft()
    if current_order <= 0 or current_order > 10:
        continue

    current_employee = employees.pop()

    if current_order <= current_employee:
        total_pizzas += current_order
    elif current_order > current_employee:
        remaining_order = current_order - current_employee
        total_pizzas += current_employee
        orders.appendleft(remaining_order)

employees_as_str = ', '.join(str(x) for x in employees)
orders_as_str = ', '.join(str(x) for x in orders)

if not orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
else:
    print(f'Not all orders are completed.')
    print(f'Orders left: {orders_as_str}')

if employees:
    print(f'Employees: {employees_as_str}')
