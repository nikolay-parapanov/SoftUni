n = int(input())
dict = {}

for i in range(n):
    input_data = input().split("<->")
    plant = input_data[0]
    rarity = input_data[1]
    rating = 0
    counter = 0
    if plant in dict.keys():
        dict[plant][0] = rarity
    else:
        dict[plant] = []
        dict[plant].append(rarity)
        dict[plant].append(rating)
        dict[plant].append(counter)

command_list = []
command = input()
while command != "Exhibition":
    list_big = command.split(": ")
    command_list.append(list_big[0])                #Command
    task = command_list[0]
    plant_reset= list_big[1]

    if task == "Reset":
        plant = plant_reset
        if plant not in dict.keys():
            print('error')
        else:
            dict[plant][1] = 0
            dict[plant][2] = 0
    else:

        second_string = list_big[1]
        list_small = second_string.split(" - ")
        command_list.append(list_small[0])              #Plant
        command_list.append(list_small[1])              #Rarity

        if task == "Rate":
            plant = command_list[1]
            if plant not in dict.keys():
                print('error')
            else:
                rating = int(command_list[2])
                dict[plant][1] += rating
                dict[plant][2] += 1
        elif task == "Update":
            plant = command_list[1]
            if plant not in dict.keys():
                print('error')
            else:
                new_rarity = command_list[2]
                dict[plant][0] = new_rarity

    command_list = []
    command = input()

for key, value in dict.items():
    if dict[key][1] == 0:
        average_rating = 0
        del dict[key][2]
    else:
        average_rating = dict[key][1]/dict[key][2]
        dict[key][1] = average_rating
        del dict[key][2]

print('Plants for the exhibition:')
for key, value in dict.items():
    print(f'- {key}; Rarity: {dict[key][0]}; Rating: {dict[key][1]:.2f}')
