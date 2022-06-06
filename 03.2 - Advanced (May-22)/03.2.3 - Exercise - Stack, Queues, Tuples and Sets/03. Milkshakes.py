from collections import deque

chocolates_stack = [int(x) for x in input().split(", ")]
milk_deque = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while chocolates_stack and milk_deque and milkshakes < 5:

    chocolate = chocolates_stack.pop()
    milk = milk_deque.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_deque.appendleft(milk)
        continue
    if milk <= 0:
        chocolates_stack.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_deque.append(milk)
        chocolates_stack.append(chocolate-5)

if milkshakes ==5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')

if chocolates_stack:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates_stack])}')
else:
    print(f'Chocolate: empty')

if milk_deque:
    print(f'Milk: {", ".join([str(x) for x in milk_deque])}')
else:
    print(f'Milk: empty')

