n = int(input())
dict = {}

for i in range(n):
    command_line = input().split('|')
    car = command_line[0]
    mileage = int(command_line[1])
    fuel = int(command_line[2])
    dict[car] = []
    dict[car].append(mileage)
    dict[car].append(fuel)

input_line = input()
while input_line != "Stop":
    command_list = input_line.split(" : ")
    task = command_list[0]

    if task == 'Drive':
        car = command_list[1]
        distance = int(command_list[2])
        fuel = int(command_list[3])

        if dict[car][1] < fuel:
            print('Not enough fuel to make that ride')
        else:
            dict[car][0] += distance
            dict[car][1] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

        if dict[car][0] >= 100000:
            del dict[car]
            print(f'Time to sell the {car}!')

    elif task == 'Refuel':
        car = command_list[1]
        fuel = int(command_list[2])

        if dict[car][1] + fuel > 75:
            fuel = 75 - dict[car][1]

        dict[car][1] += fuel
        print(f'{car} refueled with {fuel} liters')

    elif task == 'Revert':
        car = command_list[1]
        kilometers = int(command_list[2])

        dict[car][0] -= kilometers
        if dict[car][0] < 10000:
            dict[car][0] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

    input_line = input()


for key, value in dict.items():
    print(f"{key} -> Mileage: {dict[key][0]} kms, Fuel in the tank: {dict[key][1]} lt.")