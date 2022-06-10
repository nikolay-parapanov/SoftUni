n = int(input())

matrix = []
for _ in range (n):
    matrix.append([int(x) for x in input().split()])

# print(matrix)

primary = 0
secondary = 0

for rows_index in range(n):
    primary += matrix[rows_index][rows_index]
    secondary += matrix[rows_index][n-1-rows_index]

result = abs(primary - secondary)
print(result)
