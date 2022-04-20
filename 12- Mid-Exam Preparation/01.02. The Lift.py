<<<<<<< HEAD
total = int(input())

list_status = input()
list = list_status.split()
list = [int(x) for x in list]

for i in range(len(list)):
    if list[i] < 4:
        if list[i] + total >= 4:
            needed = 4- list[i]
            total -= needed
            list[i] = 4
        else:
            if list[i] + total <= 4:
                list[i] += total
                total = 0
            else:
                total = 4- list[i]
                list[i] = 4

if total == 0:
    if list[-1] == 4:
        pass
    else:
        print('The lift has empty spots!')
else:
    print(f"There isn't enough space! {total} people in a queue!")

list = [str(x) for x in list]
print(" ".join(list))
=======
total = int(input())

list_status = input()
list = list_status.split()
list = [int(x) for x in list]

for i in range(len(list)):
    if list[i] < 4:
        if list[i] + total >= 4:
            needed = 4- list[i]
            total -= needed
            list[i] = 4
        else:
            if list[i] + total <= 4:
                list[i] += total
                total = 0
            else:
                total = 4- list[i]
                list[i] = 4

if total == 0:
    if list[-1] == 4:
        pass
    else:
        print('The lift has empty spots!')
else:
    print(f"There isn't enough space! {total} people in a queue!")

list = [str(x) for x in list]
print(" ".join(list))
>>>>>>> 5af0e8593d75ee7777d6e9e2d40a1533e880b584
