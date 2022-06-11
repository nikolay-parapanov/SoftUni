input_line = input().split("|")

matrix = []
for input_section in input_line:
    matrix.append(input_section.split())

matrix.reverse()

for row in matrix:
    for item in row:
        print(item, end= " ")