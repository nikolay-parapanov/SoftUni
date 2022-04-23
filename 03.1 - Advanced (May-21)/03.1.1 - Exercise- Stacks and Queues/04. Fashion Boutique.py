from collections import deque

input_line = input().split()
stack = deque()

rack_capacity = int(input())
current_rack = rack_capacity
rack_counter = 1

for item in input_line:
    stack.append(int(item))

while len(stack)>0:
    item= stack.pop()
    if current_rack >= item:
        current_rack -= item

    else:
        rack_counter +=1
        current_rack = rack_capacity
        if current_rack >= item:
            current_rack -= item
print(rack_counter)
