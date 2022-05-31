string = input()

user_input = input()

while user_input != "Generate":

    command = user_input.split(">>>")
    task = command[0]

    if task == 'Contains':
        substring = command[1]
        if substring in string:
            print(f'{string} contains {substring}')
        else:
            print('Substring not found!')

    elif task == 'Flip':
        type = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        slice = string[start_index:end_index]
        if type == "Upper":
            slice = slice.upper()
        else:
            slice = slice.lower()
        string = string[:start_index] + slice + string[end_index:]
        print(string)

    elif task == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        string1 = string[:start_index]
        string2 = string[end_index:]
        string = string1 + string2
        print(string)
    user_input = input()

print(f'Your activation key is: {string}')