from collections import deque

effects = deque(int(x) for x in input().split(', '))
casings = [int(x) for x in input().split(', ')]

# 40: 'Datura Bombs',
# 60: 'Cherry Bombs',
# 120: 'Smoke Decoy Bombs'
db_counter, cb_counter, sdb_counter = 0, 0, 0
pouch_flag = False

while effects and casings:
    current_effect = effects.popleft()
    current_casing = casings.pop()

    current_sum = current_effect + current_casing
    if current_sum == 40:
        db_counter += 1
    elif current_sum == 60:
        cb_counter += 1
    elif current_sum == 120:
        sdb_counter += 1
    else:
        current_casing -= 5
        casings.append(current_casing)
        effects.appendleft(current_effect)

if db_counter == 3 and cb_counter == 3 and sdb_counter == 3:
    pouch_flag = True


effects_str = ', '.join(str(x) for x in effects)
casings_str = ', '.join(str(x) for x in casings)

if pouch_flag:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")


if effects:
    print(f'Bomb Effects: {effects_str}')
else:
    print(f'Bomb Effects: empty')

if casings:
    print(f'Bomb Casings: {casings_str}')
else:
    print(f'Bomb Casings: empty')

print(f'Cherry Bombs: {cb_counter}')
print(f'Datura Bombs: {db_counter}')
print(f'Smoke Decoy Bombs: {sdb_counter}')

