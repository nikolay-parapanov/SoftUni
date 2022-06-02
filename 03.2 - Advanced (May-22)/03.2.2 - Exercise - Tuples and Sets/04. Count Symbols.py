user_input = input()

dict = {}

for char in user_input:
    if char not in dict:
        dict[char] = 0
    dict[char] += 1

result = sorted(dict)

for key,value in sorted(dict.items()):
    print(f'{key}: {value} time/s')