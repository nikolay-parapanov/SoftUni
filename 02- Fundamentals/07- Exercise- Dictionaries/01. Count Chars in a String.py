input_string = input()
dictionary = dict()

for letter in input_string:
    if letter == " ":
        continue
    if letter not in dictionary:
        dictionary[letter] = 0
    dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")