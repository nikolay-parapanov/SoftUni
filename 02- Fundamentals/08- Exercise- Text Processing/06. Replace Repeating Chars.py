input = str(input())
new_str = ""

for index in range(0,len(input)-1):
    if input[index] != input[index+1]:
        new_str += input[index]


new_str = new_str + input[-1]

print(new_str)