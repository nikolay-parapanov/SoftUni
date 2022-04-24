n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_left = 0
sum_right = 0

for i in range(n):
    sum_left += matrix[i][i]
    sum_right += matrix[i][n-i-1]

diff = abs(sum_left- sum_right)

print(diff)
