list = list(map(int, input().split("@")))

command_list = input().split(" ")
current_index = 0
counter = 0
while "Love!" not in command_list:
    step = int(command_list[1])
    current_index = current_index + step

    if current_index > len(list)-1:
        current_index = 0
    if list[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    elif list[current_index] == 2:
        list[current_index] -=2
        print(f"Place {current_index} has Valentine's day.")
    else:
        list[current_index] -= 2

    last_index = current_index
    command_list = input().split(" ")

for item in list:
    if item != 0:
        counter += 1

print(f"Cupid's last position was {last_index}.")
if counter == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
