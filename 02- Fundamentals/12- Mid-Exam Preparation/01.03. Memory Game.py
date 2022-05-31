<<<<<<< HEAD
list = input()
list = list.split()
new_list = []
number_of_moves = 0

while True:
    command_line = input()
    number_of_moves += 1
    if command_line == 'end':
        break
    else:
        command = command_line.split()
        index1 = int(command[0])
        index2 = int(command[1])

        if  index1 <0 or index1 > len(list) or index2 <0 or index2 > len(list) or index1 == index2:
            index_mid = len(list)/2
            index_mid = int(index_mid)
            value = '-'+str(number_of_moves) + 'a'
            list.insert(index_mid, value)
            list.insert(index_mid, value)
            print(f'Invalid input! Adding additional elements to the board')
        else:
            if list[index1] == list[index2]:
                print(f'Congrats! You have found matching elements - {list[index1]}!')
                list = [x for x in list if x != list[index1]]
            else:
                print('Try again!')
        if len(list) == 0:
            print(f'You have won in {number_of_moves} turns!')
            break
if len(list) != 0:
    print(f'Sorry you lose :(')
=======
list = input()
list = list.split()
new_list = []
number_of_moves = 0

while True:
    command_line = input()
    number_of_moves += 1
    if command_line == 'end':
        break
    else:
        command = command_line.split()
        index1 = int(command[0])
        index2 = int(command[1])

        if  index1 <0 or index1 > len(list) or index2 <0 or index2 > len(list) or index1 == index2:
            index_mid = len(list)/2
            index_mid = int(index_mid)
            value = '-'+str(number_of_moves) + 'a'
            list.insert(index_mid, value)
            list.insert(index_mid, value)
            print(f'Invalid input! Adding additional elements to the board')
        else:
            if list[index1] == list[index2]:
                print(f'Congrats! You have found matching elements - {list[index1]}!')
                list = [x for x in list if x != list[index1]]
            else:
                print('Try again!')
        if len(list) == 0:
            print(f'You have won in {number_of_moves} turns!')
            break
if len(list) != 0:
    print(f'Sorry you lose :(')
>>>>>>> 5af0e8593d75ee7777d6e9e2d40a1533e880b584
    print(" ".join(list))