input_list = input().split(", ")

command_line = input().split(" - ")

while "Craft!" not in command_line:

    command = command_line[0]

    if command == "Combine Items":
        list2 = command_line[1].split(":")
        item_old = list2[0]
        item_new = list2[1]
        for index in range(len(input_list)):
            if input_list[index] == item_old:
                input_list.insert(index + 1, item_new)
    else:
        item = command_line[1]
        if command == "Collect":
            if item not in input_list:
                input_list.append(item)
        elif command == "Drop":
            if item in input_list:
                input_list.remove(item)
        elif command == "Renew":
            for index in range(len(input_list)):
                if input_list[index] == item:
                    last= input_list.pop(index)
                    input_list.append(last)

    command_line = input().split(" - ")

print(", ".join(input_list))

