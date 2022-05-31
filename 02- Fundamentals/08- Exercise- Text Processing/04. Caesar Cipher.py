input_str = str(input())
new_str = ""

for item in input_str:
    new_str += chr(ord(item)+3)

print(new_str)