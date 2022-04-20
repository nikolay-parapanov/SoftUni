sequence = input()
sequence = sequence.split()
sequence = [int(x) for x in sequence]
counter = 0
while True:

    command = input()
    if command == 'End':
        break
    else:
        index = int(command)

        if index >= 0 and index <= len(sequence) - 1:
            current_target_value = sequence[index]
            for i in range(len(sequence)):

                if sequence[i] != -1 and sequence[i] > current_target_value:
                    sequence[i] -= current_target_value
                elif sequence[i] != -1 and sequence[i] <= current_target_value:
                    sequence[i] += current_target_value
            sequence[index] = -1
            counter +=1
        else:
            continue
sequence = [str(x) for x in sequence]
print(f'Shot targets: {counter} -> {" ".join(sequence)}')