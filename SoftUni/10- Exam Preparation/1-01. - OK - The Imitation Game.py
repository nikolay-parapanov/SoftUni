starting_string = input()

command = input()
while command != "Decode":

    command_list = command.split("|")
    if command_list[0] == "ChangeAll":
        substring = command_list[1]
        replacement = command_list[2]
        starting_string = starting_string.replace(substring, replacement)

    elif command_list[0] == "Insert":
        index = int(command_list[1])
        value = command_list[2]
        starting_string = starting_string[:index] + value + starting_string[index:]

    elif command_list[0] == "Move":
        number_of_letters = int(command_list[1])
        starting_string = starting_string[number_of_letters:] + starting_string[:number_of_letters]

    command = input()
print(f'The decrypted message is: {starting_string}')

