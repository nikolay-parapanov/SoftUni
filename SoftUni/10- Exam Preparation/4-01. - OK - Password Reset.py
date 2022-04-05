string = input()
new_string = ''

while True:
    command = input()
    if command != "Done":
        command_list = command.split()

        if command_list[0] == "TakeOdd":
            for i in range(len(string)):
                if i % 2 != 0:
                    new_string += string[i]
            string = new_string
            print(string)

        elif command_list[0] == "Cut":
            index = int(command_list[1])
            length = int(command_list[2])
            cut = string[index:index+length]
            string = string.replace(cut, "", 1)

            print(string)

        if command_list[0] == "Substitute":
            substring = command_list[1]
            substitute = command_list[2]
            if substring in string:
                string = string.replace(substring, substitute)
                print(string)
            else:
                print('Nothing to replace!')
    else:
        break

print(f"Your password is: {string}")

