def read_matrix(rows):
    matrix = []

    for i in range(r):
        matrix.append([x for x in input().split()])

    return matrix

r, c = [int(x) for x in input().split()]
matrix = read_matrix(r)
print(matrix)
while True :
    command_line = input().split()
    if command_line == ['END']:
        break
    else:
        command = command_line[0]

        if command != "swap":
            print('Invalid input!')
            continue

        el1_idx_1, el1_idx_2 = int(command_line[1]), int(command_line[2])
        el2_idx_1, el2_idx_2 = int(command_line[3]), int(command_line[4])

        if 0 > el1_idx_1 or el1_idx_1 > r or 0 > el2_idx_1 or el2_idx_1 > r:
            print('Invalid input!')
            continue
        if 0 > el1_idx_2 or el1_idx_2 > c or 0 > el2_idx_2 or el2_idx_2 > c:
            print('Invalid input!')
            continue

        help = matrix[el1_idx_1][el1_idx_2]
        matrix[el1_idx_1][el1_idx_2] = matrix[el2_idx_1][el2_idx_2]
        matrix[el2_idx_1][el2_idx_2] = help

        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=" ")
            print()
