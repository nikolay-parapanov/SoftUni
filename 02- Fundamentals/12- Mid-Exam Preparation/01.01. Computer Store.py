<<<<<<< HEAD

sum_gross = 0
sum_net = 0
while True:
    input_line = input()
    if input_line == 'special':
        disc = 0.9
        break
    elif input_line == 'regular':
        disc = 1
        break
    else:
        price = float(input_line)
        if price <= 0:
            print(f'Invalid price!')
        else:
            sum_net += price

sum_gross = sum_net * 1.2
sum_final = sum_gross * disc

if sum_net == 0:
    print(f'Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {sum_net:.2f}$')
    print(f'Taxes: {sum_net * 0.2:.2f}$')
    print(f'-----------')
    print(f'Total price: {sum_final:.2f}$')
=======

sum_gross = 0
sum_net = 0
while True:
    input_line = input()
    if input_line == 'special':
        disc = 0.9
        break
    elif input_line == 'regular':
        disc = 1
        break
    else:
        price = float(input_line)
        if price <= 0:
            print(f'Invalid price!')
        else:
            sum_net += price

sum_gross = sum_net * 1.2
sum_final = sum_gross * disc

if sum_net == 0:
    print(f'Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {sum_net:.2f}$')
    print(f'Taxes: {sum_net * 0.2:.2f}$')
    print(f'-----------')
    print(f'Total price: {sum_final:.2f}$')
>>>>>>> 5af0e8593d75ee7777d6e9e2d40a1533e880b584
