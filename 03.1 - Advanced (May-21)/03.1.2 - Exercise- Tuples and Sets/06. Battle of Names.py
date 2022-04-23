n = int(input())

set_odd = set()
set_even = set()

for row in range(1, n+1):
    name = input()
    sum_ascii = 0
    for letter in name:
        sum_ascii += ord(letter)
    result = int(sum_ascii/row)

    if result % 2 ==0:
        set_even.add(result)
    else:
        set_odd.add(result)
final_set = set()
if sum(set_odd) == sum(set_even):
    final_set = set_odd.union(set_even)
elif sum(set_odd) > sum(set_even):
    final_set = set_odd.difference(set_even)
elif sum(set_odd) < sum(set_even):
    final_set = set_odd.symmetric_difference(set_even)

final_set = [str(x) for x in final_set]
print(", ".join(final_set))
#
# print(set_even)
# print(set_odd)
