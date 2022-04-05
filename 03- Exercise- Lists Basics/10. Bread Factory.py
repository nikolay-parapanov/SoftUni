input_list = input().split("|")

energy = 100
coins = 100
closed = False
for item in input_list:
    current_item = item.split("-")
    current_item_name = current_item[0]
    current_item_points = int(current_item[1])

    if current_item_name == "rest":
        if energy + current_item_points <= 100:
            energy += current_item_points
            print(f"You gained {current_item_points} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained 0 energy.")
            print(f"Current energy: 100.")
    elif current_item_name == "order":
        if energy >= 30:
            energy -= 30
            coins += current_item_points
            print(f"You earned {current_item_points} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= current_item_points:
            print(f"You bought {current_item_name}.")
            coins -= current_item_points
        else:
            print(f"Closed! Cannot afford {current_item_name}.")
            closed = True
            break

if not closed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")