sequence = input().split()
sequence = list(map(int, sequence))

while True:

    command = input()
    if command == 'End':
        break
    else:
        command = command.split()
        task = command[0]
        index = int(command[1])

        if task == 'Shoot':
            power = int(command[2])
            if 0<=index <= len(sequence):
                sequence[index] -= power
                if sequence[index] <= 0:
                    sequence.pop(index)

        elif task == 'Add':
            value = int(command[2])
            if 0 <= index <= len(sequence):
                sequence.insert(index, value)
            else:
                print('Invalid placement!')
        elif task == 'Strike':
            radius = int(command[2])
            index_start = index - radius
            index_end = index + radius
            if index_start <0 or index_end >len(sequence)-1:
                print('Strike missed!')
            else:
                for i in range(index_start, index_end+1):
                    sequence[i] = 'to_be_removed'
                sequence = [x for x in sequence if x!= 'to_be_removed']

sequence = [str(x) for x in sequence]
print("|".join(sequence))