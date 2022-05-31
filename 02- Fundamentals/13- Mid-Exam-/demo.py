sequence = [1, 2, 3, 3, 2, 4, 5, 3, 2]
print(sequence)
old_value = 3
new_value = 100
if old_value in sequence:
    index = sequence.index(old_value)
    sequence[index] = new_value
print(sequence)