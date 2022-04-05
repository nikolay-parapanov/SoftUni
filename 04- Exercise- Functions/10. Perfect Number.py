def check_perfect(a):
    sum_divisors = 1
    for i in range(2, a):
        if a % i == 0:
            sum_divisors += i

    if sum_divisors == a:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


user_input = int(input())
check_perfect(user_input)
