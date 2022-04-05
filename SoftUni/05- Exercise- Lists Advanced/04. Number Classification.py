input = input().split(", ")
input_int = list(map(int, input))

list_positive = [str(item) for item in input_int if item >= 0]
list_negative = [str(item) for item in input_int if item < 0]
list_even = [str(item) for item in input_int if item %2 == 0]
list_odd = [str(item) for item in input_int if item %2 != 0]

print(f"Positive: {', '.join(list_positive)}")
print(f"Negative: {', '.join(list_negative)}")
print(f"Even: {', '.join(list_even)}")
print(f"Odd: {', '.join(list_odd)}")
