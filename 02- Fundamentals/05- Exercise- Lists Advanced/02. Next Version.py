input = input().split(".")

number_str = "".join(input)
number_int = int(number_str)
number_int += 1
number_str = str(number_int)
output_list = []

for item in number_str:
    output_list.append(item)

print(".".join(output_list))