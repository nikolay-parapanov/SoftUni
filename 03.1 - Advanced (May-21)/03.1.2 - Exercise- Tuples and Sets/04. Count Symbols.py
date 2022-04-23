input_line = input()

dict = {}
for symbol in input_line:
    if symbol not in dict:
        dict[symbol] = 0
    dict[symbol] += 1


for letter in sorted(dict):
    print(f'{letter}: {dict[letter]} time/s')
