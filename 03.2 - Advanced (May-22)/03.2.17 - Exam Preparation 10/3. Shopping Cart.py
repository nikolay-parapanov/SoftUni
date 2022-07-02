def shopping_cart(*args):
    result = ''
    dict = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    for item in args:
        if item == "Stop":
            break
        dish, ingredient = item[0], item[1]
        if dish == "Soup" and len(dict[dish]) < 3 and ingredient not in dict[dish]:
            dict[dish].append(ingredient)
        if dish == "Pizza" and len(dict[dish]) < 4 and ingredient not in dict[dish]:
            dict[dish].append(ingredient)
        if dish == "Dessert" and len(dict[dish]) < 2 and ingredient not in dict[dish]:
            dict[dish].append(ingredient)

    sorted_dict = sorted(dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for tuple in sorted_dict:
        type, item = tuple
        items_sorted = sorted(item)
        result += f'{type}:\n'
        for item in items_sorted:
            result += f' - {item}\n'
    if dict["Soup"] ==[] and dict["Pizza"] ==[] and dict["Dessert"] ==[]:
        return f'No products in the cart!'
    return result

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print("-----"*40)
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print("-----"*40)
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
