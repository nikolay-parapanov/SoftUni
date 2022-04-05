input = input().split(" ")

result = []

check = [item for item in input if len(item) % 2 ==0]
result += check

print("\n".join(result))
