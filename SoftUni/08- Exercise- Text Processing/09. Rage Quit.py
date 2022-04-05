input = input()
input += " "
current_str = ""
new_str = ""
items_used = ""
counter = 0
digit_str = ""

for index in range(len(input) - 1):

    if not input[index].isdigit():
        current_str += input[index].upper()
        if input[index].upper() not in items_used:
            items_used += input[index].upper()
            counter += 1

    elif input[index].isdigit():
        if input[index + 1].isdigit():
            digit_str += input[index]
        else:
            digit_str += input[index]
            new_str += current_str * int(digit_str)
            digit_str = ""
            current_str = ""

digit_str += input[-1]

if current_str != "":
    new_str += current_str * int(digit_str)

print(f"Unique symbols used: {counter}")
print(new_str)
