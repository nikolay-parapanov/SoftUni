def chars(a, b):
    result = list()
    lower_number = ord(a)
    higher_number = ord(b)

    for i in range(lower_number+1, higher_number):
        print(chr(i),end=" ")


first_char = input()
second_char = input()
chars(first_char, second_char)

