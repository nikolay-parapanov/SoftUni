import re

user_input = input()
digits_list = []
for symbol in user_input:
    if symbol.isdigit():
        digits_list.append(int(symbol))


treshold = 1
for item in digits_list:
    treshold *= item



regex = r'(::[A-Z][a-z]{2,}::)|(\*\*[A-Z][a-z]{2,}\*\*)'

matches = re.findall(regex, user_input)


clean_list =[]

for tuple1 in matches:
    for item in tuple1:
        if item != "":
            clean_list.append(item)


cool_list = []
for item in clean_list:
    ascii_sum = 0
    for index in range(2, len(item)-2):
        ascii_sum += ord(item[index])
    if ascii_sum > treshold:
        cool_list.append(item)

print(f'Cool threshold: {treshold}')
print(f'{len(clean_list)} emojis found in the text. The cool ones are:')

for item in cool_list:
    print(item)