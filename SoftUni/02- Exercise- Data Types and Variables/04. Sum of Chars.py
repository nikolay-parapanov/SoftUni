n = int(input())
total = 0
for i in range (1, n+1):
    current_input = input()
    total += ord(current_input)

print(f"The sum equals: {total}")