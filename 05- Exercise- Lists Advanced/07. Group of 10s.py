input_list_raw = list(map(int, input().split(", ")))
input_list_reworked = input_list_raw
max = max(input_list_raw)
if max % 10 == 0:
    boundary = max
else:
    boundary = max + 10
fors = boundary // 10
list = []

for interval in range(1, fors + 1):
    list = [item for item in input_list_reworked if item <= (interval * 10)]

    input_list_reworked = [x for x in input_list_reworked if x not in list]

    print(f"Group of {interval}0's: {list}")
    list = []
