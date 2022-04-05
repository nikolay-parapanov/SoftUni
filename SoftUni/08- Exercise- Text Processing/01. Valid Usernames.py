input_list = input().split(", ")
final_list = []
flag = True
for item in input_list:
    flag = True
    if 3 >= len(item) or len(item) >= 16:
        flag = False

    for char in item:
        if not (char.isalnum() or char == "-" or char == "_"):
            flag = False

    if flag == True:
        final_list.append(item)

print("\n".join(final_list))
