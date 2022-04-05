number_lines = int(input())
capacity = 255
total_collected = 0
for i in range (1, number_lines + 1):
    current_number = int(input())
    if current_number <= (capacity - total_collected):
        total_collected += current_number
    else:
        print(f"Insufficient capacity!")
        continue

print(total_collected)