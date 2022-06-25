size = 6
matrix = []
for row_idx in range(size):
    row_input = input().split()
    matrix.append(row_input)

col_thrown = []
points_counter = 0
for throws in range(3):

    row, col = [int(x) for x in input()[1:-1].split(", ")]
    row, col = int(row), int(col)

    if row >= size or col >= size:
        continue
    if matrix[row][col] == "B" and col not in col_thrown:
        for row_idx in range(size):
            if matrix[row_idx][col] != "B":
                points_counter += int(matrix[row_idx][col])

    col_thrown.append(col)
if 100 <= points_counter <= 199:
    print(f"Good job! You scored {points_counter} points, and you've won Football.")
elif 200 <= points_counter <= 299:
    print(f"Good job! You scored {points_counter} points, and you've won Teddy Bear.")
elif points_counter >= 300:
    print(f"Good job! You scored {points_counter} points, and you've won Lego Construction Set.")
else:
    print(f'Sorry! You need {100 - points_counter} points more to win a prize.')