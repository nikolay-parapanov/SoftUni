from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers_list = ['rose', 'tulip', 'lotus', 'daffodil']

rose = {letter: False for letter in 'rose'}
tulip = {letter: False for letter in 'tulip'}
lotus = {letter: False for letter in 'lotus'}
daffodil = {letter: False for letter in 'daffodil'}

word_found = 0
flower_found = ''
while not word_found and vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key in rose:
        if key == current_vowel or key == current_consonant:
            rose[key] = True
    for key in tulip:
        if key == current_vowel or key == current_consonant:
            tulip[key] = True
    for key in lotus:
        if key == current_vowel or key == current_consonant:
            lotus[key] = True
    for key in daffodil:
        if key == current_vowel or key == current_consonant:
            daffodil[key] = True

    if all(rose.values()):
        word_found = True
        flower_found = 'rose'
    if all(tulip.values()):
        word_found = True
        flower_found = 'tulip'
    if all(lotus.values()):
        word_found = True
        flower_found = 'lotus'
    if all(daffodil.values()):
        word_found = True
        flower_found = 'daffodil'

if word_found:
    print(f'Word found: {flower_found}')
else:
    print('Cannot find any word!')

remaining_vowels_str = ' '.join(x for x in vowels)
remaining_consonants_str = ' '.join(x for x in consonants)
if vowels:
    print(f'Vowels left: {remaining_vowels_str}')
if consonants:
    print(f'Consonants left: {remaining_consonants_str}')