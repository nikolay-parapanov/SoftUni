string = input()

while True:
    command = input()
    if command == "Travel":
        break
    else:

        command_list = command.split(':')
        task = command_list[0]

        if task == "Add Stop":
            index = int(command_list[1])
            addition = command_list[2]

            if 0<= index <= len(string):
                string = string[:index] + addition + string[index:]
            print(string)
        elif task == "Remove Stop":
            start_index = int(command_list[1])
            end_index = int(command_list[2])

            if 0<= start_index <= end_index <= len(string)-1:
                string = string[:start_index]+ string[end_index+1:]
            print(string)
        elif task == "Switch":
            old_string = command_list[1]
            new_string = command_list[2]

            string = string.replace(old_string, new_string)
            print(string)

print(f'Ready for world tour! Planned stops: {string}')