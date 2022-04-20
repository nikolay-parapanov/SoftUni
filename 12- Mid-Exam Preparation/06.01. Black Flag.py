days = int(input())
plunder_per_day = float(input())
expected_plunder = float(input())

total = 0
for i in range(1, days + 1):
    total += plunder_per_day
    if i % 3 == 0:
        total += plunder_per_day*0.5
    if i % 5 == 0:
        total = total - total * 0.3

if total >= expected_plunder:
    print(f'Ahoy! {total:.2f} plunder gained.')
else:
    print(f'Collected only {(total/expected_plunder*100):.2f}% of the plunder.')
