input_list = input().split(" ")
updated_list = []
number_sublist = []
item_list = []
item_list_updated = []
for item in input_list:
    item_list = list(item)
    for index in range(0, len(item_list)):
        if item_list[index].isdigit():
            number_sublist.append(item_list[index])
        else:
            item_list_updated.append(item_list[index])

    number_int= int("".join(number_sublist))

    number_sublist = []
    first_letter = chr(number_int)
    item_list_updated.insert(0, first_letter)
    help = item_list_updated[1]
    item_list_updated[1] = item_list_updated[-1]
    item_list_updated[-1]=help
    item_list_final = "".join(item_list_updated)
    updated_list.append(item_list_final)
    item_list_updated = []

print(" ".join(updated_list))