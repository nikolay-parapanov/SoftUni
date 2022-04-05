message = input()

command = input()

while command != "Reveal":
    command_list = command.split(':|:')
    task = command_list[0]

    if task == 'InsertSpace':
        index = int(command_list[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif task == 'Reverse':
        substring = command_list[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            substring_reversed = substring[::-1]
            message += substring_reversed
            print(message)
        else:
            print('error')

    elif task == 'ChangeAll':
        substring_old = command_list[1]
        replacement_text = command_list[2]
        message = message.replace(substring_old, replacement_text)
        print(message)

    command = input()

print(f'You have a new text message: {message}')

