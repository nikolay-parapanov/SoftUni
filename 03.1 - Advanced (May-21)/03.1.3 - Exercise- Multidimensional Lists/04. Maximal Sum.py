import sys

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = -sys.maxsize
current_point = tuple()
for i in range (rows - 2):
    for j in range (cols - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + \
                      matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + \
                      matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if max_sum < current_sum:
            max_sum = current_sum
            current_point = [i,j]

i, j = current_point

print(f'Sum = {max_sum}')
for idx1 in range(i, i+2+1):
    for idx2 in range(j, j+2+1):
        print(matrix[idx1][idx2], end=" ")
    print()