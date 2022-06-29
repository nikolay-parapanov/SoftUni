import sys


def best_list_pureness(*args):
    list = args[0]
    rotation_max = args[1]
    max = -sys.maxsize
    max_rotation = 0
    rotation_count = 0

    while rotation_count <= rotation_max:
        current_sum = 0
        for idx in range(len(list)):
            current_sum += list[idx] * idx
        if current_sum > max:
            max = current_sum
            max_rotation = rotation_count
        rotation_count += 1
        if list:
            item = list.pop()
            list.insert(0, item)
        else:
            return f'Best pureness {0} after {0} rotations'
    return f'Best pureness {max} after {max_rotation} rotations'


# print(list)
# print(rotation_count)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
