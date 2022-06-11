r, c = [int(x) for x in input().split()]

input_string = str(input())

matrix = []

for rows_index in range (r):
    matrix.append([])
    for cols_index in range(c):
        matrix[rows_index].append('')

counter = 1

for rows_index in range(r):
    if rows_index %2 == 0:
        for cols_index in range(c):
            matrix[rows_index][cols_index] = input_string[(counter % len(input_string))-1]
            counter += 1
    else:
        for cols_index in range(c-1, -1, -1):
            matrix[rows_index][cols_index] = input_string[(counter % len(input_string))-1]
            counter += 1


for row in matrix:
    print(*row, sep="")