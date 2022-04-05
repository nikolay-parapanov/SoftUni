dict = {}
lang_subm = {}
command = input()

while command != "exam finished":

    if "banned" in command:
        command_list = command.split("-")
        username = command_list[0]
        del dict[username]
    else:
        command_list = command.split("-")

        username = command_list[0]
        language = command_list[1]
        points = int(command_list[2])

        if language not in lang_subm:
            lang_subm[language] = 0
        lang_subm[language] += 1

        if username not in dict:
            dict[username] = points
        else:
            if dict[username] < points:
                dict[username] = points

    command = input()

print("Results:")
for keys, values in dict.items():
    print(f"{keys} | {values}")
print("Submissions:")
for keys, values in lang_subm.items():
    print(f"{keys} - {values}")