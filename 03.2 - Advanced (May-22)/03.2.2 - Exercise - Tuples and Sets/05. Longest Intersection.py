n = int(input())

longest_intersection = []
for _ in range(n):
    user_input = input().split("-")

    section1, section2 = user_input
    section1_start, section1_end = [int(x) for x in section1.split(",")]
    section2_start, section2_end = [int(x) for x in section2.split(",")]

    intersection_start = max(section1_start, section2_start)
    intersection_end = min(section1_end, section2_end)

    current_intersection = [x for x in range(intersection_start, intersection_end + 1)]
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')
# print(section1_start, section1_end, section2_start, section2_end)
