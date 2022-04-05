budget = float(input())
price_flour = float(input())



price_eggs = 0.75 * price_flour
price_milk = 1.25 * price_flour /4
remaining_budget = budget
price_per_bread = price_flour + price_eggs + price_milk
counter_breads = 0
counter_eggs = 0

while price_per_bread < remaining_budget:
    counter_breads += 1
    counter_eggs += 3
    if counter_breads % 3 == 0:
        counter_eggs = counter_eggs - (counter_breads - 2)
    remaining_budget -= price_per_bread

print(f"You made {counter_breads} loaves of Easter bread! Now you have {counter_eggs} eggs and {remaining_budget:.2f}BGN left.")
