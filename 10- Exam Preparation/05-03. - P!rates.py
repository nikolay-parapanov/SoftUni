command_line = input()
dict = {}

while command_line != "Sail":
    command = command_line.split('||')
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city in dict.keys():
        dict[city][0] += population
        dict[city][1] += gold
    else:
        dict[city] = []
        dict[city].append(population)
        dict[city].append(gold)

    command_line = input()

command_line = input()

while command_line != 'End':

    command = command_line.split('=>')
    task = command[0]
    town = command[1]

    if task == 'Plunder':
        people = int(command[2])
        gold = int(command[3])

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        dict[town][0] -= people
        dict[town][1] -= gold

        if dict[town][0] <= 0 or dict[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del dict[town]

    elif task == 'Prosper':
        gold = int(command[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dict[town][1]} gold.")
    command_line = input()

if dict == {}:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(dict)} wealthy settlements to go to:")
    for key, value in dict.items():
        print(f'{key} -> Population: {dict[key][0]} citizens, Gold: {dict[key][1]} kg')