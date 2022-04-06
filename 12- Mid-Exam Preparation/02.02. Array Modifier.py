list = input()
list = list.split()
list = [int(x) for x in list]

while True:

    command_line = input()
    if command_line == 'end':
        break
    else:
        command = command_line.split()
        task = command[0]
        if task == 'decrease':
            list = [x-1 for x in list]
        else:
            index1 = int(command[1])
            index2 = int(command[2])
            if task == "swap":
                help = list[index1]
                list[index1] = list[index2]
                list[index2] = help
            else:
                list[index1] = list[index1]*list[index2]

list = [str(x) for x in list]
print(", ".join(list))
