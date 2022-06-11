import sys


def eggs_collection(r, c, matrix):
    biggest_sum = -sys.maxsize
    biggest_sum_path = []
    best_direction = ''
    directions = {
        'up': lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
        'left': lambda r, c: (r, c - 1),
        'right': lambda r, c: (r, c + 1)
    }

    for direction in directions:
        current_sum = 0
        row, col = directions[direction](bunny_row, bunny_col)
        current_path =[]

        while 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
            current_sum += int(matrix[row][col])
            current_path.append([row, col])
            row, col = directions[direction](row, col)

        if biggest_sum < current_sum and current_path:
            biggest_sum = current_sum
            best_direction = direction
            biggest_sum_path = current_path

    print(best_direction)
    print(*biggest_sum_path, sep= "\n")
    print(biggest_sum)


size = int(input())

field = []
for _ in range(size):
    field.append([x for x in input().split()])

for row_index in range(size):
    for col_index in range(size):
        if field[row_index][col_index] != 'B':
            continue
        bunny_row = row_index
        bunny_col = col_index

        result = eggs_collection(bunny_row, bunny_col, field)
