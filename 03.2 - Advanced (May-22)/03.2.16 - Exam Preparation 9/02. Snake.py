size = int(input())
matrix = []
snake_row, snake_col = 0, 0
burrow_coord = []

for row_idx in range(size):
    row = []
    row_input = input()
    for col_idx in range(size):
        row.append(row_input[col_idx])
    matrix.append(row)

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix)):
        if matrix[row_idx][col_idx] == "S":
            snake_row = row_idx
            snake_col = col_idx
        elif matrix[row_idx][col_idx] == "B":
            burrow_coord.append((row_idx, col_idx))

print(snake_row, snake_col)
print(burrow_coord[0])
b1_row, b1_col = burrow_coord[0]
b2_row, b2_col = burrow_coord[1]
