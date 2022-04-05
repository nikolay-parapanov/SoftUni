n = int(input())
dict = {}

for _ in range (n):
    piece_data = input().split("|")
    piece = piece_data[0]
    author = piece_data[1]
    k = piece_data[2]

    dict[piece] = []
    dict[piece].append(author)
    dict[piece].append(k)

command = input()
while command != "Stop":
    command_list = command.split("|")
    command = command_list[0]
    piece = command_list[1]

    if command == "Add":
        if piece in dict.keys():
            print(f'{piece} is already in the collection!')
        else:
            dict[piece] = []
            dict[piece].append(command_list[2])
            dict[piece].append(command_list[3])
            print(f'{piece} by {command_list[2]} in {command_list[3]} added to the collection!')
    elif command == "Remove":
        if piece in dict.keys():
            del dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        if piece in dict.keys():
            dict[piece][1] = command_list[2]
            print(f"Changed the key of {piece} to {command_list[2]}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()
for key,value in dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")