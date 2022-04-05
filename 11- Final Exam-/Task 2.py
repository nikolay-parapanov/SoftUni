import re

n = int(input())

regex = r'^\$([A-Z][a-z]{2,})\$\:\ (\[\d+\]\|)(\[\d+\]\|)(\[\d+\]\|)$|^\%([A-Z][a-z]{2,})\%\:\ (\[\d+\]\|)(\[\d+\]\|)(\[\d+\]\|)$'


for i in range (n):
    command = input()
    matches = re.findall(regex, command)

    clean_list= []
    for tuple in matches:
        for item in tuple:
            if item != '':
                if item[0] == '[':
                    clean_list.append(item[1:-2])
                else:
                    clean_list.append(item)

    if len(clean_list) == 4:
        author = clean_list[0]
        message = chr(int(clean_list[1])) + chr(int(clean_list[2])) +chr(int(clean_list[3]))
        print(f'{author}: {message}')
    else:
        print('Valid message not found!')
