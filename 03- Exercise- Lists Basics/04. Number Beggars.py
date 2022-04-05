input_list = [int(num) for num in input().split(", ")]
input_beggars = int(input())

beggars_list = [0] * input_beggars

count = 0

for i in range(len(input_list)):
    beggars_list[count] += input_list[i]
    count += 1
    if count >= input_beggars:
        count = 0

print(beggars_list)