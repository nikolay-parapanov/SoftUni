records_dict = {}
n = int(input())

for i in range(n):
    command = input()
    command_list = list(command.split())

    if command_list[0] == "register":
        user = command_list[1]
        licence = command_list[2]
        if user in records_dict:
            print(f"ERROR: already registered with plate number {licence}")
        else:
            records_dict[user] = licence
            print(f"{user} registered {licence} successfully")

    if command_list[0] == "unregister":
        user = command_list[1]
        if user not in records_dict:
            print(f"ERROR: user {user} not found")
        else:
            del(records_dict[user])
            print(f"{user} unregistered successfully")

for value in records_dict:
    print(f"{value} => {records_dict[value]}")