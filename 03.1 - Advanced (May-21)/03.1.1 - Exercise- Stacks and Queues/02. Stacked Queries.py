from collections import deque

numbers = int(input())
stack = deque()

for idx in range (numbers):
    command_line = input().split()
    command = command_line[0]

    if command == '1':
        number = int(command_line[1])
        stack.append(int(number))
    elif command == '2':
        if len(stack)>0:
            stack.pop()
    elif command == '3':
        if len(stack)>0:
            print(max(stack))
    elif command == '4':
        if len(stack) > 0:
            print(min(stack))

reversed_stack = []
while len(stack) >0 :
    reversed_stack.append(str(stack.pop()))
print(', '.join(reversed_stack))