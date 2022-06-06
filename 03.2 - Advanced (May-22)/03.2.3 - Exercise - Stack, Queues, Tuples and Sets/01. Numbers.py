set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())
operations = int(input())

for _ in range(operations):
    operation_input = input().split()
    command = operation_input[0]
    target_set = operation_input[1]

    if command == "Add":
        if target_set == "First":
            set1 = set1.union([int(x) for x in operation_input[2:]])
        else:
            set2 = set2.union([int(x) for x in operation_input[2:]])

    elif command == "Remove":
        if target_set == "First":
            set1 = set1.difference([int(x) for x in operation_input[2:]])
        else:
            set2 = set2.difference([int(x) for x in operation_input[2:]])

    else:
        print(set1.issubset(set2) or set2.issubset(set1))

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")
