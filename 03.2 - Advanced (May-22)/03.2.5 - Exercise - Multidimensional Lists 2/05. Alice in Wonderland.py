def command(r, c, direction):
    directions = {
        'up': lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
        'left': lambda r, c: (r, c - 1),
        'right': lambda r, c: (r, c + 1),
    }
    r, c = directions[direction](r, c)
    return (r, c)


n = int(input())

alice_row = 0
alice_col = 0
tea_bags_count = 0

territory = []
for ri in range(n):
    row_elements = input().split()
    for ci in range(n):
        if row_elements[ci] == 'A':
            alice_row = ri
            alice_col = ci
    territory.append(row_elements)

command_line = input()
exit_flag = 0

while command_line:
    territory[alice_row][alice_col] = "*"
    new_r, new_c = command(alice_row, alice_col, command_line)

    if 0 <= new_r < n and 0 <= new_c < n:
        alice_row, alice_col = new_r, new_c
    else:
        exit_flag = 1
        break

    if territory[new_r][new_c] == "R":
        exit_flag = 1
        break
    if territory[new_r][new_c] == '*' or territory[new_r][new_c] == '.':
        command_line = input()
        continue

    tea_bags_count += int(territory[new_r][new_c])
    if tea_bags_count >= 10:
        break
    command_line = input()

territory[alice_row][alice_col] = "*"

if exit_flag:
    print("Alice didn't make it to the tea party.")

elif tea_bags_count>=10:
    print("She did it! She went to the party.")

for i in range(n):
    for j in range(n):
        print(territory[i][j], end=" ")
    print()
