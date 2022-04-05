def check(password):
    length = False
    alnum = False
    two_dig = False
    counter_dig = 0
    if 6 <= len(password) <= 10:
        length = True

    if password.isalnum():
        alnum = True

    for item in password:
        if item.isdigit():
            counter_dig += 1

    if counter_dig >= 2:
        two_dig = True

    if length and alnum and two_dig:
        print(f"Password is valid")
    if length == False:
        print(f"Password must be between 6 and 10 characters")
    if alnum == False:
        print(f"Password must consist only of letters and digits")
    if two_dig == False:
        print(f"Password must have at least 2 digits")


user_input = input()
check(user_input)
