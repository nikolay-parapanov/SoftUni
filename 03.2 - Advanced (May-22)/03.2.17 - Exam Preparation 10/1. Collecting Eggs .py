from collections import deque

eggs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))
# print(eggs)
# print(papers)

boxes_filled_counter = 0
while eggs and papers:
    while eggs and eggs[0] <= 0:
        eggs.popleft()

    if not eggs:
        break
    current_egg = eggs.popleft()
    if current_egg == 13:
        switch_help = papers[0]
        papers[0] = papers[-1]
        papers[-1] = switch_help
        if not eggs:
            break
        current_egg = eggs.popleft()
        if current_egg < 0:
            continue

    current_paper = papers.pop()
    sum = current_egg + current_paper

    if sum <= 50:
        boxes_filled_counter += 1

eggs_str = ", ".join(str(x) for x in eggs)
papers_str = ", ".join(str(x) for x in papers)

if boxes_filled_counter > 0:
    print(f"Great! You filled {boxes_filled_counter} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {eggs_str}")

if papers:
    print(f"Pieces of paper left: {papers_str}")
