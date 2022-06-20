from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials = [int(x) for x in input().split()]
counter = 0
gifts_counter = 0
energy_spent = 0

while elves_energy and materials:
    counter += 1
    gifts_made, needed_energy, reward = 0, 0, 0

    current_elf_energy = elves_energy.popleft()
    current_box_materials = materials.pop()
    if current_elf_energy < 5:
        materials.append(current_box_materials)
        counter -= 1
        continue
    if (current_elf_energy < current_box_materials) or (
            counter % 3 == 0 and current_elf_energy < current_box_materials * 2):
        materials.append(current_box_materials)
        elves_energy.append(current_elf_energy * 2)
    else:
        if counter % 3 != 0 and counter % 5 != 0:
            needed_energy = current_box_materials
            gifts_made = 1
            reward = 1
        elif counter % 3 == 0 and counter % 5 != 0:
            needed_energy = current_box_materials * 2
            gifts_made = 2
            reward = 1
        elif counter % 3 != 0 and counter % 5 == 0:
            needed_energy = current_box_materials
            gifts_made = 0
            reward = 0

        current_elf_energy -= needed_energy
        gifts_counter += gifts_made
        energy_spent += needed_energy
        elves_energy.append(current_elf_energy + reward)

print(f'Toys: {gifts_counter}')
print(f'Energy: {energy_spent}')
if elves_energy:
    print(f'Elves left: {", ".join(str(x) for x in elves_energy)}')
if materials:
    print(f'Boxes left: {", ".join(str(x) for x in materials)}')
