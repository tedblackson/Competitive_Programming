
n = int(input())

students = []

for _ in range(n):
    students.append(input().split('#'))

for student in students:
    print(student[0], student[1], student[2])