import re

regex = r'\b_([a-zA-Z]+)\b'
command = input()
list = []
matches = re.finditer(regex, command)

for match in matches:
    list.append(match[1])

print(",".join(list))
