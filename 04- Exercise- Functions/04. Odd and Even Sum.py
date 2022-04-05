def check(a):
    sum_even = 0
    sum_odd = 0
    for digit in a:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")

number_input = input()
check(number_input)
