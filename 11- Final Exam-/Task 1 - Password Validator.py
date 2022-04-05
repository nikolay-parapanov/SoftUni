user_input = str(input())



command_line = input()
while command_line != 'Complete':
    command = command_line.split()
    task = command[0]

    if task == "Make":
        direction = command[1]
        index_make = int(command[2])

        if direction == "Upper":
            change = user_input[index_make].upper()
            user_input = user_input[:index_make] + change + user_input[index_make + 1:]
            print(user_input)
        elif direction == "Lower":
            change = user_input[index_make].lower()
            user_input = user_input[:index_make] + change + user_input[index_make + 1:]
            print(user_input)

    elif task == "Insert":
        index_insert = int(command[1])
        char = command[2]
        if 0 <= index_insert <= len(user_input):
            user_input = user_input[:index_insert] + char + user_input[index_insert:]
            print(user_input)

    elif task == "Replace":
        char = command[1]
        value = int(command[2])
        if char in user_input:
            char_value = ord(char)
            new_char_value = char_value + value
            new_char = chr(new_char_value)
            user_input = user_input.replace(char, new_char)
            print(user_input)

    elif task == "Validation":
        flag_length = True
        if len(user_input) <= 8:
            flag_length = False

        flag_symbol = True
        for symbol in user_input:
            if not symbol.isalpha() and not symbol.isdigit() and symbol != "_":
                flag_symbol = False

        flag_upper = False
        flag_lower = False
        flag_digit = False

        for symbol in user_input:
            if symbol.isupper() == True:
                flag_upper = True
            elif symbol.islower() == True:
                flag_lower = True
            elif symbol.isdigit() == True:
                flag_digit = True

        if not flag_length:
            print(f'Password must be at least 8 characters long!')
        if not flag_symbol:
            print(f'Password must consist only of letters, digits and _!')
        if not flag_upper:
            print(f'Password must consist at least one uppercase letter!')
        if not flag_lower:
            print(f'Password must consist at least one lowercase letter!')
        if not flag_digit:
            print(f'Password must consist at least one digit!')

    command_line = input()
