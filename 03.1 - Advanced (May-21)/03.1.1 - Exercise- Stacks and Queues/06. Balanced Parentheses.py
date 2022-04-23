from collections import deque

input_line = input()
flag = 1
stack = deque()
for symbol in input_line:
    if symbol in ['(', '{', '[']:
        stack.append(symbol)
    else:
        if stack:
            opening = stack.pop()
            if opening == '(' and symbol == ')':
                pass
            elif opening == '[' and symbol == ']':
                pass
            elif opening == '{' and symbol == '}':
                pass
            else:
                flag = 0
                break

        else:
            flag = 0

if len(stack)==0 and flag==1:
    print("YES")
else:
    print("NO")