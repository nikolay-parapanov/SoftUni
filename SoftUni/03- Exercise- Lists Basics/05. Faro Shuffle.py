input_list = input().split(" ")
count_shuffles = int(input())

working_list = input_list.copy()
loop_number = len(working_list)
loop_number = int(loop_number/2)
shuffle_list = []
list_a = []
list_b = []


for i in range(0, count_shuffles):
        list_a = working_list[0:loop_number]
        list_b = working_list[loop_number:]
        shuffle_list = []
        for index in range (0, loop_number):
            shuffle_list. append(list_a[index])
            shuffle_list. append(list_b[index])
        working_list = shuffle_list

print(working_list)