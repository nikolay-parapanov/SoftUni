from collections import deque
from math import ceil

r, c = [int(x) for x in input().split()]

string= input()
len_str= len(string)

total_cells = r*c
multiplier = ceil(total_cells/len_str)
string_long = string * multiplier
queue = deque()
for letter in string_long:
    queue.append(letter)

matrix = []
for i in range(r):
    matrix.append([])
    for j in range(c):
        matrix[i].append('')

for i in range(1, r+1):
    if i% 2 == 0 :
        for j in range (c-1, 0-1, -1):
            matrix[i-1][j] = queue.popleft()
    else:
        for j in range(c):
            matrix[i-1][j] = queue.popleft()

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end='')
    print()
