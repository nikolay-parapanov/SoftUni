
dictionary = dict()

while True:
    input_line_1 = input()

    if input_line_1 == "stop":
        break
    else:
        input_line_2 = input()
        if input_line_1 not in dictionary:
            dictionary[input_line_1] = 0
        dictionary[input_line_1] += int(input_line_2)

for key, value in dictionary.items():
    print(f"{key} -> {value}")
