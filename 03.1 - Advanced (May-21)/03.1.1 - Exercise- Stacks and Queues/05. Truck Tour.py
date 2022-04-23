from collections import deque

queue = deque()
n = int(input())

for _ in range(n):
    row = input().split()
    queue.append([int(row[0]), int(row[1])])

for i in range(n):
    fuel_tank = 0
    gas_pumps_travelled = 0

    for gas_pump in queue:
        fuel, distance_to_next = gas_pump[0], gas_pump[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next:
            break
        fuel_tank -= distance_to_next
        gas_pumps_travelled += 1

    if gas_pumps_travelled == len(queue):
        print(i)
        break

    queue.rotate(-1)