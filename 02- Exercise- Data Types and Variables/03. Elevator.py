people = int(input())
max = int(input())

full_course = people // max
if people % max == 0:
    print(full_course + 0)
else:
    print(full_course + 1)
