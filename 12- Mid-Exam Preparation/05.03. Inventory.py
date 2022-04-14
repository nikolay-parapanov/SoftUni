list = input().split(', ')

while True:

    command = input()
    if command == 'Craft!':
        break
    else:
        command = command.split(' - ')
        task = command[0]
        item = command[1]
        if task == 'Collect':
            flag_exist = 0
            for i in range(len(list)):
                if list[i] == item:
                    flag_exist = 1
            if not flag_exist:
                list.append(item)
        elif task == "Drop":
            flag_exist = 0
            for i in range(len(list)):
                if list[i] == item:
                    flag_exist = 1
            if flag_exist:
                list.remove(item)
        elif task == 'Combine Items':
            item = item.split(':')
            old_item = item[0]
            new_item = item[1]
            flag_exist = 0
            for i in range(len(list)):
                if list[i] == old_item:
                    flag_exist = 1
            if flag_exist:
                index = list.index(old_item)
                list.insert(index+1, new_item)
        elif task == 'Renew':
            flag_exist = 0
            for i in range(len(list)):
                if list[i] == item:
                    flag_exist = 1
            if flag_exist:
                list.remove(item)
                list.append(item)

print(', '.join(list))