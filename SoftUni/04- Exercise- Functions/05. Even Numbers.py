def even_calc(a):
    list_even= list()
    for item in user_input_as_int:
        if item % 2 ==0:
            list_even.append(item)

    print(list_even)


user_input = input().split(" ")
user_input_as_int = list(map(int, user_input))
even_calc(user_input_as_int)

