n = int(input())

set = set()
for _ in range(n):
    current_input = input().split()
    for item in current_input:
        set.add(item)

for item in set:
    print(item)
