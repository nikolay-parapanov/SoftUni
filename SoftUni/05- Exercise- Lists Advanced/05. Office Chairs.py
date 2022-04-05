rooms = int(input())
free_chairs= 0
flag = True
for room in range(1, rooms + 1):
    command = input().split(" ")
    available_chairs = len(command[0])
    people = int(command[1])

    if available_chairs >= people:
        free_chairs += available_chairs - people
    else:
        print(f"{people - available_chairs} more chairs needed in room {room}")
        flag = False

if flag:
    print(f"Game On, {free_chairs} free chairs left")