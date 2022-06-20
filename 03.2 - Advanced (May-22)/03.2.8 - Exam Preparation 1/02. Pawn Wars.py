def move_while_pawn(row, col, board):
    flag_end_of_board = 0
    if board[row - 1][col - 1] != 'b' and board[row - 1][col + 1] != 'b':
        row_output, col_output, flag_output_game_over = row - 1, col, 0
    else:
        if board[row - 1][col - 1] == 'b':
            row_output, col_output, flag_output_game_over = row - 1, col - 1, 1
        else:
            row_output, col_output, flag_output_game_over = row - 1, col + 1, 1

    if row_output == 0:
        flag_end_of_board = 1
    board[row][col] = '-'
    board[row_output][col_output] = 'w'
    return row_output, col_output, flag_output_game_over, flag_end_of_board, board


def move_black_pawn(row, col, board):
    flag_end_of_board = 0
    if board[row + 1][col - 1] != 'w' and board[row + 1][col + 1] != 'w':
        row_output, col_output, flag_output_game_over = row + 1, col, 0
    else:
        if board[row + 1][col - 1] == 'w':
            row_output, col_output, flag_output_game_over = row + 1, col - 1, 1
        else:
            row_output, col_output, flag_output_game_over = row + 1, col + 1, 1

    if row_output == 0:
        flag_end_of_board = 1
    board[row][col] = '-'
    board[row_output][col_output] = 'b'
    return row_output, col_output, flag_output_game_over, flag_end_of_board, board

board = []

white_row, white_col = 0, 0
black_row, black_col = 0, 0

for rows_idx in range(8):
    row = [x for x in input().split()]
    for col_idx in range(8):
        if row[col_idx] == 'w':
            white_row = rows_idx
            white_col = col_idx
        if row[col_idx] == 'b':
            black_row = rows_idx
            black_col = col_idx
    board.append(row)

# # for row in board:
# #     print(*row, sep=" ")
# print(white_row, white_col)
# print(black_row, black_col)

turn = 0
flag_game_over = 0
flag_end_of_board_white, flag_end_of_board_black = 0, 0

while flag_game_over == 0:
    turn += 1
    if turn % 2 != 0:
        new_white_row, new_white_col, flag_game_over, flag_end_of_board_white, board = move_while_pawn(white_row,
                                                                                                       white_col, board)
        white_row, white_col = new_white_row, new_white_col
        if flag_game_over or flag_end_of_board_white:
            break
    else:
        new_black_row, new_black_col, flag_game_over, flag_end_of_board_black, board = move_black_pawn(black_row,
                                                                                                       black_col, board)
        black_row, black_col = new_black_row, new_black_col
        if flag_game_over or flag_end_of_board_black:
            break
    # print('-------' * 20)
    # for row in board:
    #     print(*row, sep=" ")
dictcol = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}

white_coordinates = str(dictcol[white_col]) + str(8-white_row)
black_coordinates = str(dictcol[black_col]) + str(8-black_row)


if flag_game_over and turn % 2 != 0:
    print(f"Game over! White win, capture on {white_coordinates}.")
if flag_game_over and turn % 2 == 0:
    print(f"Game over! Black win, capture on {black_coordinates}.")

if flag_end_of_board_white:
    print(f'Game over! White pawn is promoted to a queen at {white_coordinates}.')
if flag_end_of_board_black:
    print(f'Game over! Black pawn is promoted to a queen at {black_coordinates }.')
