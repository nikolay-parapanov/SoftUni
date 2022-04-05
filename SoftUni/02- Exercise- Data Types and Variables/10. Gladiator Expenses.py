number_losses = int(input())

helmet_p = float(input())
sword_p = float(input())
shield_p = float(input())
armor_p = float(input())

total_cost = 0
count_shield = 0
for loss in range (1, number_losses + 1):

    if loss % 2 ==0:
        total_cost += helmet_p

    if loss % 3 ==0:
        total_cost += sword_p
        if loss % 2 ==0:
            total_cost += shield_p
            count_shield += 1
            if count_shield % 2 == 0:
                total_cost += armor_p

print(f"Gladiator expenses: {total_cost:.2f} aureus")