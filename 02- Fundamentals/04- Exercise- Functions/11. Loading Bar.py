def bar(a):

    number_of_signs = int(a / 10)
    signs_str = number_of_signs * "%"

    number_of_dots = 10 - number_of_signs
    dots_str = number_of_dots * "."

    if a == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{a}% [{signs_str}{dots_str}]")
        print("Still loading...")

user_input = int(input())
bar(user_input)
