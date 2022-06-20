def words_sorting(*args):
    dict = {}
    words = [args]
    # print(words)
    for word in args:
        dict[word] = 0
        for letter in word:
            dict[word] += ord(letter)

    total_sum = 0
    for key, value in dict.items():
        total_sum += dict[key]

    # print(total_sum)
    if total_sum % 2 == 0:
        result = sorted(dict.items())
    else:
        result = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    return '\n'.join(f'{word} - {count}' for (word, count) in result)


print(words_sorting('escape', 'charm', 'mythology'))
print('''
charm - 523
escape - 625
mythology - 1004
''')
print(words_sorting('escape', 'charm', 'eye'))
print('''
escape - 625
charm - 523
eye - 323
''')
