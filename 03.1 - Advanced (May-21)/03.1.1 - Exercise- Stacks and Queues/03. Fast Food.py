from collections import deque

total_food = int(input())
queue = deque()
input_list = input().split()

top_order = 0
flag = 0
for order in input_list:
    queue.append(int(order))
    if int(order)> top_order:
        top_order = int(order)

while len(queue) > 0:
    item = queue.popleft()
    if total_food >= item:
        total_food -= item
    else:
        flag = 1
        break

print(top_order)

if flag == 1:
    queue_str = [str(x) for x in queue]
    queue_str = (" ".join(queue_str))
    queue_str = str(item) + " " + queue_str
    print('Orders left: ', end="")
    print(queue_str)
else:
    print("Orders complete")
