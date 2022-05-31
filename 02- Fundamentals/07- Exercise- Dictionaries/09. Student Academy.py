n = int(input())
students = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

for name, grade in students.items():
    avg_value = sum(grade) / len(grade)
    if avg_value >=4.5:
        print(f"{name} -> {avg_value:.2f}")
