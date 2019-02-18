n= int(input())

students = []
for i in range(2*n):
    students.append(input().split())
grades = {}
for j in range(0, len(students), 2):
    grades[students[j][0]] = float(students[j + 1][0])
result = []
num = sorted(set(grades.values()))[1]
for stu in grades.keys():
    if grades[stu] == num:
        result.append(stu)
for k in sorted(result):
    print (k)