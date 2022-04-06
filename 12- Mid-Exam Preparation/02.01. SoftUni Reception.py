from math import ceil

n1 = int(input())
n2 = int(input())
n3 = int(input())
students = int(input())

n = n1+n2+n3
hours = ceil(students/n)
additional_hours_for_rest = hours // 3

hours += additional_hours_for_rest

print(f'Time needed: {ceil(hours)}h.')