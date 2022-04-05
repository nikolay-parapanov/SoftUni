input_list = input().split("\\")

item = input_list[-1].split(".")

print(f'File name: {item[0]}\nFile extension: {item[1]}')
