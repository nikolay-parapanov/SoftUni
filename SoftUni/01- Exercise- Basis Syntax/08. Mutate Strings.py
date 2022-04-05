first_string = str(input())
second_string = str(input())

new_string = ""
for i in range (0, len(first_string)):
    if first_string[i] != second_string[i]:
        cut = second_string[i]
        new_string= second_string[0:i] + cut + first_string[i+1:]
        print(new_string)

