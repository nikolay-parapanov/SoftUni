def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def get_kinds_around_coords(row, col, matrix):
    result = []
    if matrix[row][col - 1] == 'V' or matrix[row][col - 1] == 'X':
        result.append([row, col - 1])
    if matrix[row][col + 1] == 'V' or matrix[row][col + 1] == 'X':
        result.append([row, col + 1])
    if matrix[row - 1][col] == 'V' or matrix[row - 1][col] == 'X':
        result.append([row - 1, col])
    if matrix[row + 1][col] == 'V' or matrix[row + 1][col] == 'X':
        result.append([row + 1, col])
    return result


gifts = int(input())
size = int(input())

santa_row = 0
santa_col = 0
nice_kids = 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "S":
            santa_row = row
            santa_col = col
        elif row_elements[col] == "V":
            nice_kids += 1
    matrix.append(row_elements)

nice_kids_with_presents = 0

while gifts > 0:
    line = input()
    if line == "Christmas morning":
        break
    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = get_next_pos(santa_row, santa_col, line)
    if matrix[santa_row][santa_col] == "V":
        gifts -= 1
        nice_kids_with_presents += 1
    elif matrix[santa_row][santa_col] == "C":
        kids_around = get_kinds_around_coords(santa_row, santa_col, matrix)
        for kid_row, kid_col in kids_around:
            if matrix[kid_row][kid_col] == 'V':
                nice_kids_with_presents += 1
            gifts -= 1
            matrix[kid_row][kid_col] = '-'
            if gifts == 0:
                break

    matrix[santa_row][santa_col] = "S"

if nice_kids_with_presents != nice_kids and gifts == 0:
    print(f'Santa ran out of presents!')

for row in matrix:
    print(*row, sep=" ")

if nice_kids_with_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f'No presents for {nice_kids- nice_kids_with_presents} nice kid/s.')