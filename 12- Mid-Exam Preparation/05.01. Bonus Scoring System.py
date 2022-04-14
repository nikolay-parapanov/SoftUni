number_of_students = int(input())
total_lectures = int(input())
additional_bonus = int(input())

current_bonus = 0
max_bonus = 0
max_attendances = 0
for i in range(number_of_students):
    attendance = int(input())
    current_bonus = attendance/ total_lectures * (5 + additional_bonus)
    if max_bonus < current_bonus:
        max_bonus = current_bonus
        max_attendances = attendance

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {max_attendances} lectures.')
