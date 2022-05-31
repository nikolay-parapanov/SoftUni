days_of_championship = int(input())
target_points = int(input())
number_of_swimmers = int(input())
hotel_per_day = float(input())
participation_fee = float(input())

total_cost = 0
total_cost += days_of_championship*number_of_swimmers * hotel_per_day + number_of_swimmers * participation_fee
total_points =0
previous_day_points = 0

for i in range (1, days_of_championship+1):
    current_day_points = float(input())
    total_points += current_day_points + previous_day_points * 0.05

    previous_day_points = current_day_points



if total_points >= target_points:

    total_cost = 0.75 * total_cost
    print(f'Money left to pay: {total_cost:.2f} BGN.')
    print(f'The championship was successful!')
else:
    total_cost = 0.9 * total_cost
    print(f'Money left to pay: {total_cost:.2f} BGN.')
    print(f'The championship was not successful.')

