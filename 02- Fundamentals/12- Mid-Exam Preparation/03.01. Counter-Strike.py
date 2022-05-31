<<<<<<< HEAD
energy = int(input())
battles = 0
consecutive = 0
flag = 0
while True:
    command = input()
    if command == 'End of battle':
        break
    else:
        current_energy = int(command)
        if energy - current_energy >=0:
            battles += 1
            energy -= current_energy
            consecutive += 1
            if consecutive ==3:
                energy += battles
                consecutive = 0

        else:
            print(f'Not enough energy! Game ends with {battles} won battles and {energy} energy')
            flag = 1
            break
if not flag:
=======
energy = int(input())
battles = 0
consecutive = 0
flag = 0
while True:
    command = input()
    if command == 'End of battle':
        break
    else:
        current_energy = int(command)
        if energy - current_energy >=0:
            battles += 1
            energy -= current_energy
            consecutive += 1
            if consecutive ==3:
                energy += battles
                consecutive = 0

        else:
            print(f'Not enough energy! Game ends with {battles} won battles and {energy} energy')
            flag = 1
            break
if not flag:
>>>>>>> 5af0e8593d75ee7777d6e9e2d40a1533e880b584
    print(f'Won battles: {battles}. Energy left: {energy}')