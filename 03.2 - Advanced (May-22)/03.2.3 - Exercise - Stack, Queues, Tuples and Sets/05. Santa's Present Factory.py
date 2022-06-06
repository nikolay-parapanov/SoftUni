from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_presents = {}
flag = 0

while materials and magic:
    material_current = materials.pop()
    magic_current = magic.popleft()
    result = material_current * magic_current

    if result == 0:
        if magic_current != 0:
            magic.appendleft(magic_current)
        if material_current != 0:
            materials.append(material_current)
    elif result < 0:
        materials.append(material_current + magic_current)
    else:
        if result in presents:
            toy_name = presents[result]
            if toy_name not in crafted_presents:
                crafted_presents[toy_name] = 1
            else:
                crafted_presents[toy_name] += 1
        else:
            materials.append(material_current + 15)

    if 'Doll' in crafted_presents and 'Wooden train' in crafted_presents:
        flag = 1
    if 'Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents:
        flag = 1

if flag:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(str(x) for x in reversed(materials))}')
if magic:
    print(f'Magic left: {", ".join(str(x) for x in magic)}')

for toy, count in sorted(crafted_presents.items()):
    print(f'{toy}: {count}')
