<<<<<<< HEAD
from math import ceil

n1 = int(input())
n2 = int(input())
n3 = int(input())
students = int(input())

n = n1+n2+n3
hours = ceil(students/n)
additional_hours_for_rest = hours // 3

hours += additional_hours_for_rest

=======
from math import ceil

n1 = int(input())
n2 = int(input())
n3 = int(input())
students = int(input())

n = n1+n2+n3
hours = ceil(students/n)
additional_hours_for_rest = hours // 3

hours += additional_hours_for_rest

>>>>>>> 5af0e8593d75ee7777d6e9e2d40a1533e880b584
print(f'Time needed: {ceil(hours)}h.')