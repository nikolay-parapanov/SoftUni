n, m = [ int(x) for x in input().split()]

set1 = set()
set2 = set()
for _ in range(n):
    set1.add(input())
for _ in range(m):
    set2.add(input())

result = set1.intersection(set2)
for item in result:
    print(item)