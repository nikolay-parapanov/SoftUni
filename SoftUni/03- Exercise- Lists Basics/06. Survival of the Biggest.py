input_list = input().split(" ")
numbers_to_remove = int(input())

list_as_integer = list(map(int, input_list))

for i in range (1, numbers_to_remove+1):
    current_min_element = min(list_as_integer)
    input_list.remove(str(current_min_element))
    list_as_integer.remove(current_min_element)

print(", ".join(input_list))