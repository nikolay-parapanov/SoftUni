r, c = [int(x) for x in input().split()]

# print(r, c)

matrix = []
counter = 0

for _ in range(r):
    matrix.append([x for x in input().split()])

for row_index in range(r-1):
    for col_index in range(c-1):
        if matrix[row_index][col_index] == matrix[row_index][col_index+1]== matrix[row_index+1][col_index] == matrix[row_index+1][col_index+1]:
            counter+= 1

print(counter)