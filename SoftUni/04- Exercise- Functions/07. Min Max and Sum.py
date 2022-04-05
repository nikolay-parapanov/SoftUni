def check(list_):
    min_num = min(input_list_int)
    max_num = max(input_list_int)
    sum_numbers = sum(input_list_int)

    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_numbers}")


input_list = input().split(" ")
input_list_int = list(map(int, input_list))
check(input_list_int)