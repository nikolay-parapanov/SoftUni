import re

command = input()
regex = r'\d+'
list = []

while True:
    if command:
        matches = re.findall(regex, command)
        if matches:
            print(" ".join(matches), end=" ")
        command = input()
    else:
        break

print(" ".join(list))
