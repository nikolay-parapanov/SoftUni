n = int(input())

set_even = set()
set_odd = set()

for row in range(1, n+1):
    current_name = input()
    name_sum_result = 0
    for char in current_name:
        name_sum_result += ord(char)

    name_sum_result = name_sum_result// row
    if name_sum_result % 2 == 0:
        set_even.add(name_sum_result)
    else:
        set_odd.add(name_sum_result)

sum_even = sum(set_even)
sum_odd = sum(set_odd)

if sum_even == sum_odd:
    result = set_odd.union(set_even)
elif sum_odd > sum_even:
    result = set_odd - set_even
elif sum_even > sum_odd:
    result = (set_odd - set_even) | (set_even - set_odd)

print(", ".join(str(x) for x in result))