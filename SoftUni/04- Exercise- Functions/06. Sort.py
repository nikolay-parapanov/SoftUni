def sorting(list_):
    input_list_int.sort()
    return input_list_int

input_list = input().split(" ")
input_list_int = list(map(int, input_list))
sorting(input_list_int)
print(input_list_int)


