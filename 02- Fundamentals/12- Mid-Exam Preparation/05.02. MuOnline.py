<<<<<<< HEAD
rooms = input().split('|')
health = 100
bitcoins = 0
list = []
flag = 0
for i in range(len(rooms)):
    list.append(rooms[i])
    command = list[i].split()
    task = command[0]
    points = int(command[1])

    if task == 'potion':
        if health + points > 100:
            points = 100- health
        health += points
        print(f'You healed for {points} hp.')
        print(f'Current health: {health} hp.')
    elif task == 'chest':
        bitcoins += points
        print(f'You found {points} bitcoins.')
    else:
        monster = task
        attack = points
        if health - points > 0:
            health -= points
            print(f'You slayed {monster}.')
        else:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {i+1}')
            flag = 1
            break

if not flag:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


=======
rooms = input().split('|')
health = 100
bitcoins = 0
list = []
flag = 0
for i in range(len(rooms)):
    list.append(rooms[i])
    command = list[i].split()
    task = command[0]
    points = int(command[1])

    if task == 'potion':
        if health + points > 100:
            points = 100- health
        health += points
        print(f'You healed for {points} hp.')
        print(f'Current health: {health} hp.')
    elif task == 'chest':
        bitcoins += points
        print(f'You found {points} bitcoins.')
    else:
        monster = task
        attack = points
        if health - points > 0:
            health -= points
            print(f'You slayed {monster}.')
        else:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {i+1}')
            flag = 1
            break

if not flag:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


>>>>>>> 5af0e8593d75ee7777d6e9e2d40a1533e880b584
