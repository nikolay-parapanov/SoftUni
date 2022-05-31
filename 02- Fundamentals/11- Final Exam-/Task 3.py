command_line = input()
dict = {}

while command_line != "Log out":
    command = command_line.split(': ')
    task = command[0]
    user_name = command[1]

    if task == 'New follower':
        if user_name not in dict.keys():
            dict[user_name] = []
            likes = 0
            comments = 0
            dict[user_name].append(likes)
            dict[user_name].append(comments)
    elif task == "Like":
        if user_name not in dict.keys():
            dict[user_name] = []
            likes = 0
            comments = 0
            dict[user_name].append(likes)
            dict[user_name].append(comments)

        likes = int(command[2])
        dict[user_name][0] += likes
    elif task == 'Comment':
        if user_name not in dict.keys():
            dict[user_name] = []
            likes = 0
            comments = 0
            dict[user_name].append(likes)
            dict[user_name].append(comments)
        comments = 1
        dict[user_name][1] += 1
    elif task == 'Blocked':
        if user_name in dict.keys():
            del dict[user_name]
        else:
            print(f"{user_name} doesn't exist.")
    command_line = input()

print(f'{len(dict)} followers')
for user_name, value in dict.items():
    print(f'{user_name}: {dict[user_name][0] + dict[user_name][1]}')