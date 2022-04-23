number1, number2 = input().split()
number1, number2 = int(number1), int(number2)

set1 = set()
set2 = set()
for _ in range(number1):
    set1.add(input())

for _ in range(number2):
    set2.add(input())

result = set(set1.intersection(set2))

for item in result:
    print(item)