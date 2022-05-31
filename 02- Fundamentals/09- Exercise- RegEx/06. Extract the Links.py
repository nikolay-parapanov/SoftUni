import re

sentence = input()

regex = r'((www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))'
valid_urls = []
while sentence:
    matches = re.finditer(regex, sentence)
    for match in matches:
        valid_urls.append(match.group(1))
        print(match.group(1))
    sentence = input()
#
# print(valid_urls)