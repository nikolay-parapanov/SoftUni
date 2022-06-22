from math import floor


def get_new_position(row, col, direction):
    if direction == "up":
        row -= 1
        if row < 0:
            row = size - 1
    if direction == "down":
        row += 1
        if row >= size:
            row = 0
    if direction == "left":
        col -= 1
        if col < 0:
            col = size - 1
    if direction == "right":
        col += 1
        if col >= size:
            col = 0

    return row, col


size = int(input())
player_row, player_col = 0, 0
path_record = []
matrix = []
for row_idx in range(size):
    row_input = input().split()
    for col_idx in range(size):
        if row_input[col_idx] == "P":
            player_row = row_idx
            player_col = col_idx
            path_record.append([player_row, player_col])
    matrix.append(row_input)


coins_collected = 0
wall_hit = False
coins_collected_flag = False

while coins_collected <100:
    direction = input()
    new_row, new_col = get_new_position(player_row, player_col, direction)
    matrix[player_row][player_col] = 0
    player_row, player_col = new_row, new_col
    path_record.append([player_row, player_col])

    if matrix[player_row][player_col] == "X":
        if coins_collected == 0:
            coins_collected = 0
        else:
            coins_collected = floor(coins_collected * 0.5)
        wall_hit = True
        break
    else:
        coins_collected += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = 0

    # print('---'*40)
    # for row in matrix:
    #     print(*row, sep=' ')

if coins_collected >=100:
    print(f"You won! You've collected {floor(coins_collected)} coins.")
elif wall_hit:
    print(f"Game over! You've collected {floor(coins_collected)} coins.")

print(f'Your path:')
for item in path_record:
    print(item, sep='\n')