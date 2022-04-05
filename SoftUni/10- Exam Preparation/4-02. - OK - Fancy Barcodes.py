import re

n = int(input())
regex = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
numbers_str = ''

for i in range(n):
    command = input()
    match = re.findall(regex, command)

    if match == []:
        print('Invalid barcode')
    else:
        for symbol in match[0]:
            if symbol.isdigit() == True:
                numbers_str += symbol
        if numbers_str =="":
            print('Product group: 00')
        else:
            print(f'Product group: {numbers_str}')
        numbers_str = ""