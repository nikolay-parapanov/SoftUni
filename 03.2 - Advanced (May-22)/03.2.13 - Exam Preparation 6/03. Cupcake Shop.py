from collections import deque

def stock_availability(inventory, *args):
    inventory = deque(inventory)
    args = deque(args)
    action = args.popleft()

    if action == 'delivery':
        for item in args:
            inventory.append(item)
    elif action == "sell":
        if not args:
            inventory.popleft()
        elif isinstance(args[0], int):
            items_to_remove = args[0]
            for idx in range(items_to_remove):
                inventory.popleft()
        else:
            for item in args:
                for inventory_item in [x for(x) in inventory]:
                    if inventory_item == item:
                        inventory.remove(inventory_item)

    return ([x for(x) in inventory])




print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
