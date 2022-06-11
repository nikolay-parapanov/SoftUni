def agressiveness_calculation(r, c, matrix):
    counter = 0
    if 0 <= (r - 2) < len(matrix) and 0 <= (c - 1) < len(matrix) and matrix[r - 2][c - 1] == "K":
        counter += 1
    if 0 <= (r - 1) < len(matrix) and 0 <= (c - 2) < len(matrix) and matrix[r - 1][c - 2] == "K":
        counter += 1
    if 0 <= (r + 1) < len(matrix) and 0 <= (c - 2) < len(matrix) and matrix[r + 1][c - 2] == "K":
        counter += 1
    if 0 <= (r + 2) < len(matrix) and 0 <= (c - 1) < len(matrix) and matrix[r + 2][c - 1] == "K":
        counter += 1
    if 0 <= (r + 2) < len(matrix) and 0 <= (c + 1) < len(matrix) and matrix[r + 2][c + 1] == "K":
        counter += 1
    if 0 <= (r + 1) < len(matrix) and 0 <= (c + 2) < len(matrix) and matrix[r + 1][c + 2] == "K":
        counter += 1
    if 0 <= (r - 1) < len(matrix) and 0 <= (c + 2) < len(matrix) and matrix[r - 1][c + 2] == "K":
        counter += 1
    if 0 <= (r - 2) < len(matrix) and 0 <= (c + 1) < len(matrix) and matrix[r - 2][c + 1] == "K":
        counter += 1
    return counter


n = int(input())
matrix = []
knights_removed = 0

for _ in range(n):
    matrix.append(list(input()))

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == '0':
                continue

            cur_aggressive_count = agressiveness_calculation(row_index, col_index, matrix)

            if cur_aggressive_count > best_count:
                best_count = cur_aggressive_count
                knight_row = row_index
                knight_col = col_index

    if best_count == 0:
        break

    matrix[knight_row][knight_col] = '0'
    knights_removed += 1

print(knights_removed)
