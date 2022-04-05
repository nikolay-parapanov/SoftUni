input = str(input())
strength = 0
result = ""

for index in range(len(input)):
    if input[index] == ">":
        strength += int(input[index+1])
        result += input[index]
    else:
        if strength == 0:
            result += input[index]
        if strength >0:
            strength -= 1

print(result)