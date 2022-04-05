input_list = input().split("#")
water_amount = int(input())
condition = False
total_effort = 0
total_fire = 0
print("Cells:")

for item in input_list:
    current_item = item.split(" = ")
    type_of_fire = str(current_item[0])
    value_of_fire = int(current_item[1])
    condition = False

    if 1 <= value_of_fire <= 50 and type_of_fire == "Low":
        condition = True
    elif 51 <= value_of_fire <= 80 and type_of_fire == "Medium":
        condition = True
    elif 81 <= value_of_fire <= 125 and type_of_fire == "High":
        condition = True

    if condition:
        if water_amount >= value_of_fire:
            water_amount -= value_of_fire
            total_effort += value_of_fire * 0.25
            total_fire += value_of_fire
            print(f" - {value_of_fire}")


print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

