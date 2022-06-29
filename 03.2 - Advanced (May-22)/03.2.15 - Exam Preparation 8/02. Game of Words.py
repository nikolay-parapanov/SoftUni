def get_new_coordinate(command, row, col):
    if command == "up" and row > 0:
        row -= 1
    if command == "down" and row < size - 1:
        row += 1
    if command == "left" and col > 0:
        col -= 1
    if command == "right" and col < size - 1:
        col += 1

    return row, col


str = str(input())
size = int(input())
player_row, player_col = 0, 0
matrix = []
for row_idx in range(size):
    row_input = input()
    row = []
    for col_idx in range(len(row_input)):
        row.append(row_input[col_idx])
    matrix.append(row)

# for row in matrix:
#     print(*row, sep=" ")

for row_idx in range(size):
    for col_idx in range(size):
        if matrix[row_idx][col_idx] == "P":
            player_row = row_idx
            player_col = col_idx

commands = int(input())
matrix[player_row][player_col] = "-"
for idx in range(commands):
    command = input()
    new_row, new_col = get_new_coordinate(command, player_row, player_col)
    if new_row==player_row and new_col ==player_col:
       str = str[0:-1]
       continue
    player_row, player_col = new_row, new_col
    # print(matrix[player_row][player_col])
    if matrix[player_row][player_col] != "-":
        str += matrix[player_row][player_col]
        matrix[player_row][player_col] = "-"

matrix[player_row][player_col] = "P"
print(str)
for row in matrix:
    print(*row, sep= "")
