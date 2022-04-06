list = input()
list = list.split()
list = [int(x) for x in list]

average_list = sum(list) / len(list)
list = sorted(list, key= lambda x: -x)

if len(list)<5:
    for i in range (len(list)):
        if list[i] > average_list:
            print(list[i], end= " ")
        else:
            print('No')
else:
    for i in range(5):
        if list[i] > average_list:
            print(list[i], end= " ")