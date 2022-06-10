r, c = [int(x) for x in input().split()]

starting_point = ord('a')
matrix = []

for rows_index in range(r):
    matrix.append([])
    for cols_index in range(c):
        matrix[rows_index].append(
            chr(starting_point + rows_index) + chr(starting_point + rows_index + cols_index) + chr(starting_point + rows_index))
        print()

for rows_index in range(r):
    print(" ".join(matrix[rows_index]), end="\n")
