import re

command = input()
result = []
regex = r'((?<=\s)[a-z0-9]+([\-|\.|\_][a-z0-9]+)*@[a-z]+-?[a-z]+(\.[a-z]+){1,})'

matches = re.finditer(regex, command)

for match in matches:
    result.append(match[1])

print("\n".join(result))
