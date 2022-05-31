number_snowballs = int(input())

highest_value = 0

for i in range(1, number_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    current_value = (weight / time) ** quality
    if current_value > highest_value:
        highest_value = current_value
        h_weight = weight
        h_time = time
        h_quality = quality
print(f"{h_weight} : {h_time} = {int(highest_value)} ({h_quality})")