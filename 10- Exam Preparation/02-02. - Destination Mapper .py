import re

user_input = input()
regex = r'=[A-Z][A-Za-z]{2,}=|\/[A-Z][A-Za-z]{2,}\/'
points = 0
list = re.findall(regex, user_input)

current_stripped = [i[1:-1] for i in list]

for item in current_stripped:
    points += len(item)

print(f'Destinations: {", ".join(current_stripped)}')
print(f'Travel Points: {points}')
