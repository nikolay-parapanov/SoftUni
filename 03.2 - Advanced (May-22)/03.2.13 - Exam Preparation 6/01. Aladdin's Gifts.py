def present_check(current_sum, gs_, ps_, gold_, dj_):
    if 100 <= current_sum <= 199:
        gs_ += 1
    elif 200 <= current_sum <= 299:
        ps_ += 1
    elif 300 <= current_sum <= 399:
        gold_ += 1
    elif 400 <= current_sum <= 499:
        dj_ += 1

    return gs_, ps_, gold_, dj_


from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
gs_counter, ps_counter, gold_counter, dj_counter = 0, 0, 0, 0

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    current_sum = current_material + current_magic
    if 100 <= current_sum <= 499:
        gs_counter, ps_counter, gold_counter, dj_counter = present_check(current_sum, gs_counter, ps_counter,
                                                                         gold_counter, dj_counter)
    elif current_sum < 100 and current_sum % 2 == 0:
        current_sum = current_material * 2 + current_magic * 3
        gs_counter, ps_counter, gold_counter, dj_counter = present_check(current_sum, gs_counter, ps_counter,
                                                                         gold_counter, dj_counter)
    elif current_sum < 100 and current_sum % 2 != 0:
        current_sum = current_sum * 2
        gs_counter, ps_counter, gold_counter, dj_counter = present_check(current_sum, gs_counter, ps_counter,
                                                                         gold_counter, dj_counter)
    elif current_sum > 499:
        current_sum = current_sum / 2
        gs_counter, ps_counter, gold_counter, dj_counter = present_check(current_sum, gs_counter, ps_counter,
                                                                         gold_counter, dj_counter)

flag = False
if (gs_counter > 0 and ps_counter > 0) or (gold_counter > 0 and dj_counter > 0):
    print(f'The wedding presents are made!')
else:
    print(f'Aladdin does not have enough wedding presents.')

materials_str = ', '.join(str(x) for x in materials)
magic_str = ', '.join(str(x) for x in magic)

if materials:
    print(f'Materials left: {materials_str}')
if magic:
    print(f'Magic left: {magic_str}')

if dj_counter>0:
    print(f'Diamond Jewellery: {dj_counter}')
if gs_counter>0:
    print(f'Gemstone: {gs_counter}')
if gold_counter>0:
    print(f'Gold: {gold_counter}')
if ps_counter>0:
    print(f'Porcelain Sculpture: {ps_counter}')