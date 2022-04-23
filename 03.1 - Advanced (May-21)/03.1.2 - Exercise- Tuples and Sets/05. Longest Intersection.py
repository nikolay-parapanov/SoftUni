n = int(input())
max_length = 0

for _ in range(n):
    command_line = input().split("-")
    first_line_start, first_line_end = command_line[0].split(",")
    first_line_start, first_line_end = int(first_line_start), int(first_line_end)
    second_line_start, second_line_end = command_line[1].split(",")
    second_line_start, second_line_end = int(second_line_start), int(second_line_end)
    intersection_start = max(first_line_start, second_line_start)
    intersection_end = min(first_line_end, second_line_end)
    length = intersection_end - intersection_start+1

    if max_length< length:
        max_length = length
        max_start = intersection_start
        max_end = intersection_end

result_list = []
for i in range(max_start, max_end+1):
    result_list.append(i)

print("Longest intersection is", result_list, end= "")
print(f" with length {max_length}")