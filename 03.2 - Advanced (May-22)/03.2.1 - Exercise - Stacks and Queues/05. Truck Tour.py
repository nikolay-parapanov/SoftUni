from collections import deque

pumps = int(input())

track = deque()

for _ in range(pumps):
    current_pump_data = list(int(x) for x in input().split())
    track.append(current_pump_data)
flag = True
rotation_counter = 0
for rotation_counter in range(0,len(track)-1):
    current_point = 0
    for index in range(len(track)):
        petrol = track[index][0]
        distance = track[index][1]
        if (current_point + petrol - distance) < 0:
            flag = False
            break
        else:
            current_point = current_point + petrol - distance
            flag = True
    if not flag:
        track.rotate(-1)
    else:
        output_index = rotation_counter
        flag = True
        break
if flag:
    print(output_index)
