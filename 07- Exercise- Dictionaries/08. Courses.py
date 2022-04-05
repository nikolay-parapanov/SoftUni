course_dict = {}

command = input()

while command != "end":

    command_list = list(command.split(" : "))
    course = command_list[0]
    name = command_list[1]

    if course not in course_dict:
        course_dict[course] = []
    course_dict[course].append(name)
    command = input()

for key in course_dict:
    print(f"{key}: {len(course_dict[key])}")
    for item in course_dict[key]:
        print(f"-- {item}")


