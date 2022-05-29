list = [int(x) for x in input().split()]

stack = []
for item in list:
    stack.append(item)

for _ in range (len(list)):
    print(stack.pop(), end = " ")

