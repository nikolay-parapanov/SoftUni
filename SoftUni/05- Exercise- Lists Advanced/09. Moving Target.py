input_list = list(map(int, input().split(" ")))

command_list = input().split(" ")

while "End" not in command_list:
    command = command_list[0]
    index = int(command_list[1])
    if command == "Shoot" and (0 <= index < len(input_list)):
            power = int(command_list[2])
            input_list[index] -= power
            if input_list[index] <= 0:
                input_list.pop(index)
    if command == "Add":
        if (0 <= index < len(input_list)):
            value = int(command_list[2])
            input_list.insert(index, value)
        else:
            print("Invalid placement!")
    if command == "Strike":
        radius = int(command_list[2])
        if (index - radius >= 0) and (index + radius <= len(input_list)):
            for index in range(index-radius, index+ radius + 1):
                input_list[index] = ""
        else:
            print("Strike missed!")
    input_list = [x for x in input_list if x != ""]
    command_list = input().split(" ")

output_list = list(map(str, input_list))
print("|".join(output_list))