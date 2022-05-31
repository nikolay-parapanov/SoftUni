sequence = input().split('|')


while True:
    command = input()
    if command == 'Shop!':
        break
    else:
        command = command.split('%')
        task = command[0]
        if task == "Important":
            product = command[1]
            if product in sequence:
                sequence.remove(product)
            sequence.insert(0, product)
        elif task == 'Add':
            product = command[1]
            if product not in sequence:
                sequence.append(product)
            else:
                print('The product is already in the list.')
        elif task == 'Swap':
            product1 = command[1]
            product2 = command[2]

            if product1 in sequence and product2 in sequence:
                index1 = sequence.index(product1)
                index2 = sequence.index(product2)
                help = sequence[index1]
                sequence[index1] = sequence[index2]
                sequence[index2] = help
            else:
                if product1 not in sequence:
                    print(f'Product {product1} missing!')
                elif product2 not in sequence:
                    print(f'Product {product2} missing!')
        elif task == 'Remove':
            product = command[1]
            if product in sequence:
                sequence.remove(product)
            else:
                print(f"Product {product} isn't in the list.")
        elif task == 'Reverse':
            sequence.reverse()

for i in range(len(sequence)):
    print(f'{i+1}. {sequence[i]}')