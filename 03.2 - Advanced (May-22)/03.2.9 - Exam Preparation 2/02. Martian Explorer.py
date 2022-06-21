size = 6
matrix = []


def get_new_position(row, col, command):
    if command == 'down':
        row = row + 1
    elif command == 'up':
        row = row - 1
    elif command == 'left':
        col = col - 1
    elif command == 'right':
        col = col + 1

    if row < 0:
        row = 5
    if row > 5:
        row = 0
    if col < 0:
        col = 5
    if col > 5:
        col = 0

    return row, col


rover_row, rover_col = 0, 0

for row_index in range(size):
    row_input = input().split()
    for col_index in range(size):
        if row_input[col_index] == 'E':
            rover_row = row_index
            rover_col = col_index
    matrix.append(row_input)

# for row in matrix:
#     print(*row, sep=" ")

commands_line = input().split(", ")
w_flag, m_flag, c_flag, r_flag = False, False, False, False

for command in commands_line:
    new_rover_row, new_rover_col = get_new_position(rover_row, rover_col, command)
    rover_row, rover_col = new_rover_row, new_rover_col

    if matrix[rover_row][rover_col] == "W":
        print(f'Water deposit found at ({rover_row}, {rover_col})')
        w_flag = True
    if matrix[rover_row][rover_col] == "M":
        print(f'Metal deposit found at ({rover_row}, {rover_col})')
        m_flag = True
    if matrix[rover_row][rover_col] == "C":
        print(f'Concrete deposit found at ({rover_row}, {rover_col})')
        c_flag = True
    if matrix[rover_row][rover_col] == "R":
        print(f'Rover got broken at ({rover_row}, {rover_col})')
        break

if w_flag and m_flag and c_flag:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')
