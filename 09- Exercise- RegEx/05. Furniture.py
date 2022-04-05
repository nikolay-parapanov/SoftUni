import re

#  ">>{furniture_name}<<{price}!{quantity}"

pattern = '^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$'
bought_furniture = []
total_sum = 0
command = input()

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_sum += float(price) * int(quantity)

    command = input()

print("Bought furniture:")
for item in bought_furniture:
    print(item)

print(f"Total money spend: {total_sum:.2f}")