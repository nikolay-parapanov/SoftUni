number_of_electrons = int(input())
current_electrons = number_of_electrons
list = []
n = 1

while current_electrons > 0:
    current_shell = 2 * n ** 2
    if current_shell > current_electrons:
        list.append(current_electrons)
    else:
        list.append(current_shell)

    current_electrons -= current_shell
    n += 1

print(list)