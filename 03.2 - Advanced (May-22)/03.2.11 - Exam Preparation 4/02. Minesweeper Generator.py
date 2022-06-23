def matrix_creation(size):
    field = []
    for row_idx in range(size):
        field_row = []
        for col_idx in range(size):
            field_row.append(0)
        field.append(field_row)
    return field


def populating_bomb_counters(field, row, col, size):
    counter = 0
    if field[row][col] == "*":
        return "*"
    else:
        if row - 1 >= 0 and col - 1 >= 0 and field[row - 1][col - 1] == "*":
            counter += 1
        if row - 1 >= 0 and col >= 0 and field[row - 1][col] == "*":
            counter += 1
        if row - 1 >= 0 and col + 1 <= size - 1 and field[row - 1][col + 1] == "*":
            counter += 1
        if col - 1 >= 0 and field[row][col - 1] == "*":
            counter += 1
        if col + 1 <= size - 1 and field[row][col + 1] == "*":
            counter += 1
        if row + 1 <= size - 1 and col - 1 >= 0 and field[row + 1][col - 1] == "*":
            counter += 1
        if row + 1 <= size - 1 and field[row + 1][col] == "*":
            counter += 1
        if row + 1 <= size - 1 and col + 1 <= size - 1 and field[row + 1][col + 1] == "*":
            counter += 1

        return counter


size = int(input())
bombs = int(input())

field = matrix_creation(size)

for bomb in range(bombs):
    tuple = input()[1:-1]
    # print(tuple)
    bomb_row, bomb_col = tuple.split(", ")
    bomb_row = int(bomb_row)
    bomb_col = int(bomb_col)
    field[bomb_row][bomb_col] = "*"

# for row in field:
#     print(*row, sep=" ")

    for row_idx in range(len(field)):
        for col_idx in range(len(field)):
            field[row_idx][col_idx] = populating_bomb_counters(field, row_idx, col_idx, size)
            # print("-------"*10)
            # for r in field:
            #     print(*r, sep=" ")

for row in field:
    print(*row, sep=" ")
