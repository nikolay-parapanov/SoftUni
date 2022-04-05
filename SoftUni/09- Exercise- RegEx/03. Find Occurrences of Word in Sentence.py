import re

sentence = input()
word = input()
regex = fr'(\b{word}\b)'
result = []

matches = re.finditer(regex, sentence, re.IGNORECASE)
for match in matches:
    result.append(match[1])

print(len(result))