input_substr = input().split(", ")
input_str = input().split(", ")

result = list()
for item in input_substr:
    for each_item in input_str:
        if item in each_item:
            if item not in result:
                result.append(item)


print(result)
