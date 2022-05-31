<<<<<<< HEAD
string = input()
string = string.split('@')
string = list(map(int, string))


current_index = 0
last_index = 0
count_missed = 0
while True:

    command = input()
    if command == 'Love!':
        break
    else:
        command = command.split()
        length = int(command[1])
        current_index += length
        if current_index > len(string)-1:
            current_index = 0

        if string[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            string[current_index] -= 2
            last_index = current_index
            if string[current_index] ==0:
                print(f"Place {current_index} has Valentine's day.")

print(f"Cupid's last position was {last_index}.")

for i in string:
    if i != 0:
        count_missed +=1
if count_missed ==0:
    print('Mission was successful.')
else:
=======
string = input()
string = string.split('@')
string = list(map(int, string))


current_index = 0
last_index = 0
count_missed = 0
while True:

    command = input()
    if command == 'Love!':
        break
    else:
        command = command.split()
        length = int(command[1])
        current_index += length
        if current_index > len(string)-1:
            current_index = 0

        if string[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            string[current_index] -= 2
            last_index = current_index
            if string[current_index] ==0:
                print(f"Place {current_index} has Valentine's day.")

print(f"Cupid's last position was {last_index}.")

for i in string:
    if i != 0:
        count_missed +=1
if count_missed ==0:
    print('Mission was successful.')
else:
>>>>>>> 5af0e8593d75ee7777d6e9e2d40a1533e880b584
    print(f'Cupid has failed {count_missed} places.')