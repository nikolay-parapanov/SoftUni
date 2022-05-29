clothes = [int(x) for x in input().split()]
capacity = int(input())

rack_capacity = capacity
racks_counter = 1
for _ in range(len(clothes)):
    current_item = clothes.pop()
    if rack_capacity< current_item:
        racks_counter +=1
        rack_capacity = capacity
    rack_capacity -= current_item

print(racks_counter)
