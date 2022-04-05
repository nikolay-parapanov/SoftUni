list = input().split(" ")

list_as_integer = []

for item in list:
    item = int(item)
    list_as_integer.append(-item)


print(list_as_integer)