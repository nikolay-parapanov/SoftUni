import sys

rows, cols = [int(x) for x in input().split()]

matrix = []
max_sum = -sys.maxsize
current_sum = max_sum

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for r in range(rows - 2):
    for c in range(cols - 2):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + \
                      matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] + \
                      matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            cords = (r, c)

print(f'Sum = {max_sum}')
r_max, c_max = cords
for row_index in range(r_max, r_max + 3):
    for col_index in range(c_max, c_max + 3):
        print(matrix[row_index][col_index], end=" ")
    print()
