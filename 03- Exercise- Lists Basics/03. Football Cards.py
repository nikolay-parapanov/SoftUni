input_list = input().split(" ")

penalty_list_a = []
penalty_list_b = []
condition = False
for item in input_list:
    sub_list = item.split("-")
    team = item[0]
    number = item[1]
    if team == "A":
        if item in penalty_list_a:
            pass
        else:
            penalty_list_a.append(item)
    else:
        if item in penalty_list_b:
            pass
        else:
            penalty_list_b.append(item)

    if len(penalty_list_a) > 4 or len(penalty_list_b) > 4:
        condition = True
        break
print(f"Team A - {(11 - len(penalty_list_a))}; Team B - {(11 - len(penalty_list_b))}")
if condition:
    print("Game was terminated")
