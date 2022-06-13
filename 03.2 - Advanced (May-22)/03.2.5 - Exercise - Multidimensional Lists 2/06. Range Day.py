def get_next_pos(row, col, direction, steps):
    if direction == 'up':
        return row - steps, col
    if direction == 'down':
        return row + steps, col
    if direction == 'left':
        return row, col - steps
    if direction == 'right':
        return row, col + steps


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 5

matrix = []
position_row = 0
position_col = 0
targets = 0
targets_positions = []

for ri in range(size):
    row_input = [x for x in input().split()]
    for ci in range(size):
        if row_input[ci] == "A":
            position_row = ri
            position_col = ci
        if row_input[ci] == "x":
            targets += 1
    matrix.append(row_input)

remaining_targets = targets

commands_number = int(input())
matrix[position_row][position_col] = '.'

for counter in range(commands_number):
    command_line = input().split()
    action = command_line[0]
    direction = command_line[1]
    if action == 'move':
        steps = int(command_line[2])
        new_row, new_col = get_next_pos(position_row, position_col, direction, steps)

        if is_inside(new_row, new_col, size) and matrix[new_row][new_col] == '.':
            position_row, position_col = new_row, new_col

    if action == 'shoot':
        bullet_r, bullet_c = get_next_pos(position_row, position_col, direction, 1)
        while is_inside(bullet_r, bullet_c, size):
            if matrix[bullet_r][bullet_c] == 'x':
                targets -= 1
                matrix[bullet_r][bullet_c] = '.'
                targets_positions.append([bullet_r, bullet_c])
                break
            bullet_r, bullet_c = get_next_pos(bullet_r, bullet_c, direction, 1)
        if targets == 0:
            break

if targets ==0 :
    print(f'Training completed! All {len(targets_positions)} targets hit.')
else:
    print(f'Training not completed! {targets} targets left.')

print(*targets_positions, sep="\n")


# for row in matrix:
#     print(row)
