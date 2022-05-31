quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

christmas_spirit = 0
purchase = 0

for day in range(1, days + 1):

    if day % 11 ==0:
        quantity += 2

    if day % 2 == 0:
        purchase += quantity * ornament_set
        christmas_spirit += 5

    if day % 3 == 0:
        purchase += quantity * ( tree_skirt + tree_garlands)
        christmas_spirit += 13

    if day % 5 ==0:
        purchase += quantity* tree_lights
        christmas_spirit += 17
        if day % 3 ==0:
            christmas_spirit += 30

    if day % 10 ==0:
        purchase += tree_skirt + tree_garlands + tree_lights
        christmas_spirit -= 20



if days % 10 ==0:
    christmas_spirit -= 30

print(f"Total cost: {purchase}")
print(f"Total spirit: {christmas_spirit}")