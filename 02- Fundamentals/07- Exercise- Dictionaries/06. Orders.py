orders_dict = {}
command = input()
total_orders_dict = {}
while command != "buy":

    user_input = command.split()
    product = user_input[0]
    price = float(user_input[1])
    quantity = int(user_input[2])

    if product not in orders_dict:
        orders_dict[product] = [price, quantity]
    else:
        orders_dict[product] = price, quantity + orders_dict[product][1]



    command = input()

for key in orders_dict:
    print(f"{key} -> {orders_dict[key][0]*orders_dict[key][1]:.2f}")