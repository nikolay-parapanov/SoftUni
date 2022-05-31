import re

total_calories = 0
list_products = []
days = 0
string = input()
regex = r'#([A-za-z\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([A-za-z\s]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'

matches = re.findall(regex, string)
for i in range (len(matches)):
    for item in matches[i]:
        if item != "":
            list_products.append(item)

for idx in range(2, len(list_products) + 1, 3):
    total_calories += int(list_products[idx])
days = int(total_calories/2000)

print(f'You have food to last you for: {days} days!')
for item in range (0, len(list_products), 3):
    print(f'Item: {list_products[item]}, Best before: {list_products[item + 1]}, Nutrition: {list_products[item+2]}')
