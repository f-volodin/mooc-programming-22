tuples = [ ]
import math

while True:
    score = str(input("Exam points and exercises completed: "))
    if score == "":
        break
    score = score.split()
    tuples.append(( int(score[0]) , int(score[1]) ))

grades = [ ]
points = [ ]
for item in tuples:
    i = item[0] + round(int(item[1]/10))
    point = math.floor(item[0] + item[1]/10)

    if item[0] < 10:
        s = 0
    elif 0<=i<=14:
        s = 0
    elif 15<=i<=17:
        s = 1
    elif 18<=i<=20:
        s = 2
    elif 21<=i<=23:
        s = 3
    elif 24<=i<=27:
        s = 4
    elif 28<=i<=30:
        s = 5
    grades.append(s)
    points.append(point)

average_points = sum(points) / len(points)

pass_pr = round(100-((grades.count(0)/len(grades))*100), 1)

print("Statistics:")
print(f"Points average: {average_points}")
print(f"Pass percentage: {pass_pr}")
print("Grade distribution:")
print(f"  5: {grades.count(5)*'*'}")
print(f"  4: {grades.count(4)*'*'}")
print(f"  3: {grades.count(3)*'*'}")
print(f"  2: {grades.count(2)*'*'}")
print(f"  1: {grades.count(1)*'*'}")
print(f"  0: {grades.count(0)*'*'}")