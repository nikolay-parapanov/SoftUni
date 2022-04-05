input_list = input().split("|")
budget = float(input())

condition = False
sale_list = []
profit =0
total_sales = 0

for item in input_list:
    current_item = item.split("->")
    type_of_stock = current_item[0]
    cost_of_stock = float(current_item[1])
    condition = False
    if type_of_stock == "Clothes" and cost_of_stock <= 50:
        condition = True
    if type_of_stock == "Shoes" and cost_of_stock <= 35:
        condition = True
    if type_of_stock == "Accessories" and cost_of_stock <= 20.5:
        condition = True

    if condition:
        if budget >= cost_of_stock:
            budget -= cost_of_stock
            sale_price = cost_of_stock * 1.4
            total_sales += sale_price
            profit += cost_of_stock * 0.4
            sale_list.append(f'{sale_price:.2f}')
        else:
            budget_enough = False


print(" ".join(sale_list))

print(f"Profit: {profit:.2f}")

if (total_sales+budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")