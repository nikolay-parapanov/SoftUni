number_of_orders = int(input())


total_price = 0
for order in range (1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    number_of_capsules = int(input())
    price = price_per_capsule * days * number_of_capsules
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
    price = 0

print(f"Total: ${total_price:.2f}")
