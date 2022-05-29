from collections import deque


def robots_list(robots_input):
    robots_list = robots_input.split(";")
    return robots_list


def time(time_input):
    time_list = time_input.split(":")
    hours, minutes, seconds = int(time_list[0]), int(time_list[1]), int(time_list[2])
    time_in_seconds = hours * 60 * 60 + minutes * 60 + seconds
    return time_in_seconds


def products_deque():
    products_deque = deque()
    while True:
        current_input = input()
        if current_input != "End":
            products_deque.append(current_input)
        else:
            break

    return products_deque


def seconds_string(seconds):
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds % 3600 % 60 % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

robots_input = input()
time_input = input()

robots_list = robots_list(robots_input)
current_time = time(time_input)
products_deque = products_deque()

available_robots_names_only = []
robots_dict_seconds_default = {}
working_robots = {}

for index in range(len(robots_list)):
    key, value = robots_list[index].split("-")
    robots_dict_seconds_default[key] = int(value)
    available_robots_names_only.append(key)

while products_deque:
    current_time = (current_time + 1) % (24 * 60 * 60)

    for robot_name in [k for k in working_robots.keys()]:
        working_robots[robot_name] -= 1
        if working_robots[robot_name] <= 0:
            working_robots.pop(robot_name)

    current_product = products_deque.popleft()
    for robot_name in available_robots_names_only:
        if robot_name not in working_robots:
            print(f'{robot_name} - {current_product} [{seconds_string(current_time)}]')
            working_robots[robot_name] = robots_dict_seconds_default[robot_name]
            break
    else:
        products_deque.append(current_product)
