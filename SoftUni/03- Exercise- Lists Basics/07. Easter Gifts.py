gift_list = input().split(" ")

command_line = input()

while command_line != 'No Money':
    command = command_line.split()
    task = command[0]
    gift = command[1]

    if task == "OutOfStock":
        for index in range(len(gift_list)):
            if gift_list[index] == gift:
                gift_list[index] = None

    elif task == "Required":
        req_index = int(command[2])
        if 0 < req_index < len(gift_list):
            gift_list[req_index] = gift

    elif task == "JustInCase":
        gift_list.pop(-1)
        gift_list.append(gift)

    command_line = input()

while None in gift_list:
    gift_list.remove(None)

print(" ".join(gift_list))
