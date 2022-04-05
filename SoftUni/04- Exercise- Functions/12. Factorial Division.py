def fact(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * fact(a-1)


user_input_1 = int(input())
user_input_2 = int(input())
result1 = fact(user_input_1)
result2 = fact(user_input_2)

print(f"{result1/result2:.2f}")
