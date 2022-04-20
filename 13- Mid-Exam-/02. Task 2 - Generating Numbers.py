sequence = list(map(int, input().split()))

while True:
    command = input()
    if command == 'END':
        break
    else:
        command = command.split()
        task = command[0]
        if task == 'add':
            add_list = []
            for i in range(3, len(command)):
                add_list.append(int(command[i]))
            sequence = add_list + sequence
        elif task == 'remove':
            if command[1] == 'greater':
                value_treshold = int(command[3])
                sequence = list(filter(lambda x: x <= value_treshold, sequence))
            else:
                index = int(command[3])
                if 0 <= index < len(sequence):
                    sequence.pop(index)
        elif task == 'replace':
            old_value = int(command[1])
            new_value = int(command[2])
            if old_value in sequence:
                index = sequence.index(old_value)
                sequence[index] = new_value
        elif task == 'find':
            if command[1] == 'even':
                sub_list = list(filter(lambda x: x %2==0, sequence))
                sub_list = list(map(str, sub_list))
                print(" ".join(sub_list))
                sub_list = list(str(x) for x in sub_list)
            if command[1] == 'odd':
                sub_list = list(filter(lambda x: x % 2 != 0, sequence))
                sub_list = list(map(str, sub_list))
                print(" ".join(sub_list))

sequence = list(map(str, sequence))
print(", ".join(sequence))
