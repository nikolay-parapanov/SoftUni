rows = int(input())
set = set()

for _ in range(rows):
    command = input().split()
    for item in command:
        set.add(item)

for item in set:
    print(item)