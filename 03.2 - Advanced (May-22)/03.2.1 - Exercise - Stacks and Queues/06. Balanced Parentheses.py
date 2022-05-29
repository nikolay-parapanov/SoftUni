expression_str = input()
expression_list = []
for _ in expression_str:
    expression_list.append(_)
stack = []

closing_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}
flag = True
for item in expression_list:
    if item in '([{':
        stack.append(item)
    else:
        if stack:
            ch = stack.pop()
            if item != closing_dict[ch]:
                flag = False
                break
        else:
            flag = False
            break

if not flag or stack:
    print('NO')
else:
    print('YES')
