def check(list_):
    for item in list_:
        if item == item[::-1]:
            print("True")
        else:
            print("False")


input = input().split(", ")
check(input)
