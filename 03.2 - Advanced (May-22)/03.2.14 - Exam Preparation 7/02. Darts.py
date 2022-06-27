def throw(points, row, col):
    if 0 > row or row > size - 1 or 0 > col or col > size - 1:
        pass
    else:
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            points -= int(matrix[row][col])
        elif row == 3 and col == 3:
            points = 0
        elif matrix[row][col] == "D":
            cur_result = int(matrix[0][col]) + int(matrix[size - 1][col]) + int(matrix[row][0]) + int(
                matrix[row][size - 1])
            points -= cur_result * 2
        elif matrix[row][col] == "T":
            cur_result = int(matrix[0][col]) + int(matrix[size - 1][col]) + int(matrix[row][0]) + int(
                matrix[row][size - 1])
            points -= cur_result * 3

    return points


size = 7
input_line = input().split(", ")

player1, player2 = input_line[0], input_line[1]
# print(player1,player2)
player1_score, player2_score = 501, 501

matrix = []
for row_idx in range(size):
    row_input = input().split()
    matrix.append(row_input)

# for row in matrix:
#     print(*row, sep = " ")
player1_counter, player2_counter = 0,0
turn_counter = 1
while player1_score > 0 and player2_score > 0:
    if turn_counter % 2 != 0:
        current_player = player1
        current_points = player1_score
    else:
        current_player = player2
        current_points = player2_score

    current_throw = input()[1:-1].split(", ")
    throw_row, throw_col = int(current_throw[0]), int(current_throw[1])
    new_points = throw(current_points, throw_row, throw_col)
    if turn_counter % 2 != 0:
        player1_score = new_points
        player1_counter +=1
        if player1_score <= 0:
            print(f"{player1} won the game with {player1_counter} throws!")
            break
    else:
        player2_score = new_points
        player2_counter +=1
        if player2_score <= 0:
            print(f"{player2} won the game with {player2_counter} throws!")
            break

    turn_counter += 1
