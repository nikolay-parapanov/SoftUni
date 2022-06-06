from collections import deque

expression = input().split()

operation = {
    '+' : lambda a,b: a+b,
    '-' : lambda a,b: a-b,
    '*' : lambda a,b: a*b,
    '/' : lambda a,b: a//b,
}

nums = deque()

for ch in expression:
    if ch in '+-*/':
        while len(nums) > 1:

            current_result = operation[ch](nums.popleft(), nums.popleft())
            nums.appendleft(current_result)
    else:
        nums.append(int(ch))

print(*nums, sep= "")