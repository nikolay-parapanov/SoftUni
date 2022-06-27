from collections import deque

effects = deque(int(x) for x in input().split(', '))
power = [int(x) for x in input().split(", ")]
effects2 = deque(x for x in effects if x > 0)
power2 = [x for x in power if x > 0]
# print(effects2)
# print(power2)

enough_flag = False
palm_counter, willow_counter, crossette_counter = 0, 0, 0

while not enough_flag and effects2 and power2:
    current_effect = effects2.popleft()
    current_power = power2.pop()
    sum_current = current_effect + current_power

    if sum_current % 3 == 0 and sum_current % 5 != 0:
        palm_counter += 1
    elif sum_current % 3 != 0 and sum_current % 5 == 0:
        willow_counter += 1
    elif sum_current % 3 == 0 and sum_current % 5 == 0:
        crossette_counter += 1
    else:
        current_effect -= 1
        if current_effect !=0:
            effects2.append(current_effect)
        power2.append(current_power)

    if palm_counter >= 3 and willow_counter >= 3 and crossette_counter >= 3:
        enough_flag = True

if enough_flag:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

effects2_str = ", ".join(str(x) for x in effects2)
power2_str = ", ".join(str(x) for x in power2)

if effects2:
    print(f"Firework Effects left: {effects2_str}")
if power2:
    print(f"Explosive Power left: {power2_str}")

output = f'''Palm Fireworks: {palm_counter}
Willow Fireworks: {willow_counter}
Crossette Fireworks: {crossette_counter}
'''
print(output)