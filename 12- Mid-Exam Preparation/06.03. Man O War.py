pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
max_health = int(input())
flag = 0

while True:
    command = input()
    if command == 'Retire':
        break
    else:
        command = command.split()
        task = command[0]

        if task == "Fire":
            index = int(command[1])
            damage = int(command[2])

            if 0 <= index <= len(war_ship):
                war_ship[index] -= damage
                if war_ship[index] <= 0:
                    print(f'You won! The enemy ship has sunken.')
                    break
        elif task == 'Defend':
            start_index = int(command[1])
            end_index = int(command[2])
            damage = int(command[3])

            if 0 <= start_index <= end_index <= len(pirate_ship):
                for i in range(start_index, end_index + 1):
                    pirate_ship[i] -= damage
                    if pirate_ship[i] <= 0:
                        print('You lost! The pirate ship has sunken.')
                        flag = 1
                        break

        elif task == 'Repair':
            index = int(command[1])
            health = int(command[2])
            if 0 <= index <= len(pirate_ship):
                if pirate_ship[index] + health > max_health:
                    health = max_health - pirate_ship[index]
                pirate_ship[index] += health

        elif task == 'Status':
            counter = 0
            treshold = max_health * 0.2
            for item in pirate_ship:
                if item < treshold:
                    counter += 1
            print(f"{counter} sections need repair.")

if not flag:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(war_ship)}')