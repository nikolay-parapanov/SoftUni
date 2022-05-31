from string import ascii_lowercase
from string import ascii_uppercase

def item_manipulation(item):
    result = 0
    number_as_string = ""
    for idx in range(len(item)):
        if item[idx].isnumeric():
            number_as_string += item[idx]

    number_as_int = int(number_as_string)

    for idx in range(len(item)):
        if item[idx].isalpha() and idx == 0:
            if item[idx] == item[idx].lower():
                first_lower = ascii_lowercase.index(item[idx])+1
                result1 = number_as_int * first_lower
            elif item[idx] == item[idx].upper():
                first_upper = ascii_uppercase.index(item[idx])+ 1
                result1 = number_as_int / first_upper
        elif item[idx].isalpha() and idx !=0:
            if item[idx] == item[idx].lower():
                second_lower = ascii_lowercase.index(item[idx])+1
                result2 = result1 + second_lower
            elif item[idx] == item[idx].upper():
                second_upper = ascii_uppercase.index(item[idx])+1
                result2 = result1 - second_upper

    return result2

input_list = input().split()
total_sum = 0

for item_in_list in input_list:
    total_sum += item_manipulation(item_in_list)

print(f'{total_sum:.2f}')