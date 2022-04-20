shopping_list = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break
    else:
        command = command.split()
        task = command[0]
        if task == 'Urgent':
            item = command[1]
            flag_dupl = 0
            for i in range(len(shopping_list)):
                if shopping_list[i] == item:
                    flag_dupl = 1
            if not flag_dupl:
                shopping_list.insert(0,item)
        elif task == 'Unnecessary':
            item = command[1]
            flag_dupl = 0
            for i in range(len(shopping_list)):
                if shopping_list[i] == item:
                    flag_dupl = 1
            if flag_dupl:
                shopping_list.remove(item)
        elif task == 'Correct':
            item_old = command[1]
            item_new = command[2]
            flag_dupl = 0
            for i in range(len(shopping_list)):
                if shopping_list[i] == item_old:
                    flag_dupl = 1
            if flag_dupl:
                index = shopping_list.index(item_old)
                shopping_list[index] = item_new
        elif task == 'Rearrange':
            item = command[1]
            flag_dupl = 0
            for i in range(len(shopping_list)):
                if shopping_list[i] == item:
                    flag_dupl = 1
            if flag_dupl:
                index = shopping_list.index(item)
                shopping_list.pop(index)
                shopping_list.append((item))

print(", ".join(shopping_list))

