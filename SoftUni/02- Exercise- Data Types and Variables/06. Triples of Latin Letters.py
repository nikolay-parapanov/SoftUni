number = int(input())

for i in range (0, number):
    for j in range (0, number):
        for k in range (0, number):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97+ k)}")