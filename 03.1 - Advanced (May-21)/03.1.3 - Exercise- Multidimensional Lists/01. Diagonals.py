rows = int(input())

matrix = []
for _ in range(rows):
    row_input = [int(x) for x in input().split(', ')]
    matrix.append(row_input)


sum_left = 0
sum_right = 0
list_left = []
list_right = []

for i in range(rows):
    sum_left += matrix[i][i]
    list_left.append(matrix[i][i])

    sum_right += matrix[i][rows - i - 1]
    list_right.append(matrix[i][rows - i - 1])

list_left = [str(x) for x in list_left]
list_right = [str(x) for x in list_right]
print(f'Primary diagonal:', ', '.join(list_left),end= '. ')
print(f'Sum: {sum_left}')
print(f'Secondary diagonal:', ', '.join(list_right),end= '. ')
print(f'Sum: {sum_right}')
