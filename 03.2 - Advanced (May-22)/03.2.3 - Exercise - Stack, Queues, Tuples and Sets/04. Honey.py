from collections import deque

bees_collections = deque([int(x) for x in input().split()])
nectar_collections = [int(x) for x in input().split()]
symbols_sequence = deque(input().split())

honey = 0

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}
while bees_collections and nectar_collections:
    bee = bees_collections.popleft()
    nectar = nectar_collections.pop()

    if nectar < bee:
        bees_collections.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = symbols_sequence.popleft()
    honey += abs(operators[operator](bee, nectar))

print(f'Total honey made: {honey}')

if bees_collections:
    print(f'Bees left: {", ".join([str(x) for x in bees_collections])}')

if nectar_collections:
    print(f'Bees left: {", ".join([str(x) for x in nectar_collections])}')
