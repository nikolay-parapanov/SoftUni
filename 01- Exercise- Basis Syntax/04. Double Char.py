string_input = input()
string_duplicated =""

for _ in string_input:
    string_duplicated = string_duplicated + _ + _

print(string_duplicated)
    