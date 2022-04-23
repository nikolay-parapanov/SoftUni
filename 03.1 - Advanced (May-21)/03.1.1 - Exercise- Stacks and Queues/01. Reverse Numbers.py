input = input().split()

stack = []

for i in range (len(input)):
    stack.append(input.pop())

print(" ".join(stack))

