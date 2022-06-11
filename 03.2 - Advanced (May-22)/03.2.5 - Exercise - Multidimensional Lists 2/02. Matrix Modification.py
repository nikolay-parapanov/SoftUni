n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

# print(matrix)

command_line = input().split()

while command_line[0] != "END":
    command, r, c, value = command_line[0], int(command_line[1]), int(command_line[2]), int(command_line[3])

    if not (0 <= r < n and 0 <= c <= n):
        print("Invalid coordinates")
        command_line = input().split()
        continue
    if command == "Add":
        matrix[r][c] += value
    elif command == "Subtract":
        matrix[r][c] -= value

    command_line = input().split()

for row in matrix:
    print(*row, sep=" ")

