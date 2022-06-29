from collections import deque

males1 = [int(x) for x in input().split()]
females1 = [int(x) for x in input().split()]

# print(males1)
# print(females1)

males = [x for x in males1 if x > 0]
females = deque(x for x in females1 if x > 0)

match_count = 0
while males and females:
    current_male = males.pop()
    current_female = females.popleft()

    if current_male % 25 == 0:
        males.pop()
        continue
    if current_female % 25 == 0:
        females.popleft()
        continue
    if current_male == current_female:
        match_count += 1
    else:
        current_male -= 2
        if current_male > 0:
            males.append(current_male)

print(f"Matches: {match_count}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")
