input_list = input().split()
first_word = input_list[0]
second_word = input_list[1]
sum = 0
if len(first_word) >= len(second_word):
    long_word = first_word
    short_word = second_word
else:
    short_word = first_word
    long_word = second_word

for index in range(len(short_word)):
    sum += ord(short_word[index]) * ord(long_word[index])

for index in range(len(short_word), len(long_word)):
    sum += ord(long_word[index])

print(sum)
