sentence = str(input())
list = []
for index in range(len(sentence)):
    if sentence[index] == ":" and sentence[index+ 1] != " ":
        list.append(sentence[index] + sentence[index + 1])

print("\n".join(list))