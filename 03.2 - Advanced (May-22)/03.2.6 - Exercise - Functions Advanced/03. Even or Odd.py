def even_odd(*args):
    filter_command = args[-1]
    result = []
    parity = 0 if filter_command = 'even' else 1
    for idx in range(len(args)-1):
        number = args[idx]
        if number % 2 == parity
            result.append(number)

    return result

print(even_odd(1,2,3,4,5,6,"even"))