chest = input().split('|')
total_points = 0
total_items = 0
avrg = 0
stolen = []

while True:
    command = input()
    if command == 'Yohoho!':
        break
    else:
        command = command.split()
        task = command[0]
        if task == "Loot":
            for i in range(1, len(command)):
                if command[i] not in chest:
                    chest.insert(0, command[i])
        if task == "Drop":
            index = int(command[1])
            if 0 <= index <= len(chest) - 1:
                help = chest[index]
                chest.pop(index)
                chest.append(help)
        if task == "Steal":
            count = int(command[1])
            stolen = chest[- count:]
            chest = chest[:-count]
            print(', '.join(stolen))

for item in chest:
    total_items += 1
    for letter in item:
        total_points += 1

if len(chest) ==0:
    print(f'Failed treasure hunt.')
else:
    avrg = total_points / total_items
    print(f'Average treasure gain: {avrg:.2f} pirate credits.')