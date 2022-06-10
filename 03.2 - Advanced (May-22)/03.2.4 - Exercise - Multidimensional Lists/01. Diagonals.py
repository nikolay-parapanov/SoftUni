size = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for rows_index in range(size):
    matrix.append([int(x) for x in input().split(", ")])

for rows_index in range(size):
    primary_diagonal.append(matrix[rows_index][rows_index])
    secondary_diagonal.append(matrix[rows_index][size - 1 - rows_index])

# print(matrix)
print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')

