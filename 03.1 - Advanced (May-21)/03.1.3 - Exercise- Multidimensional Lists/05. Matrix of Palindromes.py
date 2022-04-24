r, c = [int(x) for x in input().split()]

matrix = []

for i in range(r):
    matrix.append([])
    for j in range(c):
        matrix[i].append(chr(i+97) + chr(j+97+i) + chr (i+97))


for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()