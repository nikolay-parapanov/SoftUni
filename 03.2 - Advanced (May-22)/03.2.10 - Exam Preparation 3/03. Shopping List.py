def shopping_list(budget, **kwargs):
    result = ''
    remaining_budget = budget
    products_limit = 5

    if budget < 100:
        result += 'You do not have enough budget.\n'
    else:
        for product_name, product_details in kwargs.items():
            product_price, product_quantity = product_details
            if remaining_budget > product_price * product_quantity and products_limit>0:
                result += f'You bought {product_name} for {(product_price * product_quantity):.2f} leva.\n'
                remaining_budget -= product_price * product_quantity
                products_limit -=1

    return result

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
