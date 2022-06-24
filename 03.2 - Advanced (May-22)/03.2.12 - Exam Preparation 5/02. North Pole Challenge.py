def get_new_coordinates(row, col, command):
    if command == 'right':
        col = (col + 1) % columns
    if command == 'left':
        col = (col - 1) % columns
    if command == "up":
        row = (row - 1) % rows
    if command == "down":
        row = (row + 1) % rows

    return row, col


rows, columns = [int(x) for x in input().split(', ')]

matrix = []
items_counter = 0
for row_idx in range(rows):
    row_input = input().split()
    for col_idx in range(columns):
        if row_input[col_idx] == "Y":
            my_row = row_idx
            my_col = col_idx
        if row_input[col_idx] in ["G", "D", "C"]:
            items_counter +=1
    matrix.append(row_input)

d_counter = 0
g_counter = 0
c_counter = 0
flag = False
while True:
    if flag:
        break
    command_line = input().split("-")
    command = command_line[0]
    if command == "End":
        break
    else:
        matrix[my_row][my_col]= 'x'
        step = int(command_line[1])
        for x in range(step):
            new_row, new_col = get_new_coordinates(my_row, my_col, command)
            if matrix[new_row][new_col] == "D":
                d_counter += 1
                items_counter -= 1
            elif matrix[new_row][new_col] == "G":
                g_counter += 1
                items_counter -= 1
            elif matrix[new_row][new_col] == "C":
                c_counter += 1
                items_counter -=1
            matrix[new_row][new_col] = "x"
            my_row, my_col = new_row, new_col
            if items_counter == 0:
                flag = True
                break

matrix[my_row][my_col] = "Y"

if items_counter == 0:
    print(f'Merry Christmas!')
print(f"You've collected:")
print(f'- {d_counter} Christmas decorations')
print(f'- {g_counter} Gifts')
print(f'- {c_counter} Cookies')

for row in matrix:
    print(*row, sep = " ")


