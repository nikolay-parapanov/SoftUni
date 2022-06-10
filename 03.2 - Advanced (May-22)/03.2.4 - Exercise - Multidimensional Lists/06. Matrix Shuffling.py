r, c = [int(x) for x in input().split()]

matrix = []

for row_index in range(r):
    matrix.append([x for x in input().split()])

# print(matrix)

command_line = input().split()

while command_line[0] != "END":
    if len(command_line) == 5:
        command, row1, col1, row2, col2 = str(command_line[0]), int(command_line[1]), int(command_line[2]), int(command_line[3]), int(command_line[4])
    else:
        print(f'Invalid input!')
        command_line = input().split()
        continue
    if command == "swap" and 0 <= row1 < r and 0 <= row2 < r and 0 <= col1 < c and 0 <= col2 < c:
        help_var = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = help_var
    else:
        print(f'Invalid input!')
        command_line = input().split()
        continue
    for row_print in range(r):
        for col_print in range(c):
            print(matrix[row_print][col_print], end=" ")
        print()

    command_line = input().split()
