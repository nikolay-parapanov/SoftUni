names_input = input().split(", ")
player1_name = names_input[0]
player2_name = names_input[1]

size = 6
matrix = []
for row_idx in range(size):
    row_input = input().split()
    for col_idx in range(size):
        if row_input[col_idx] == "E":
            exit_row = row_idx
            exit_col = col_idx
    matrix.append(row_input)

# for row in matrix:
#     print(*row, sep=" ")
flags_waiting = {}
flags_waiting[player1_name] = False
flags_waiting[player2_name] = False

turn = 1
flag_waiting = 0
flag_end = False
while not flag_end:
    coordinates_line = input().strip("()").split(", ")
    if not coordinates_line:
        break
    row, col = int(coordinates_line[0]), int(coordinates_line[1])

    if turn % 2 != 0:
        current_player_name, secondary_player = player1_name, player2_name
    else:
        current_player_name, secondary_player = player2_name, player1_name
    if flags_waiting[current_player_name] == True:
        flags_waiting[current_player_name] = False
        turn += 1
        continue
    if matrix[row][col] == "E":
        print(f"{current_player_name} found the Exit and wins the game!")
        flag_end = True
    elif matrix[row][col] == "T":
        print(f"{current_player_name} is out of the game! The winner is {secondary_player}.")
        flag_end = True
    elif matrix[row][col] == "W":
        print(f"{current_player_name} hits a wall and needs to rest.")
        flags_waiting[current_player_name] = True
    turn += 1
