import math
def points_exam(list_x, list_y):
    exams = sum(list_x) / len(list_x)
    exercises = (sum(list_y) / len(list_y)) / 10
    return round((exams + exercises), 2 )
def pass_pr(list_x):
    lister = [ ]
    for i in list_x:
        if i < 10:
            pass
        else:
            lister.append(i)
    return round(((len(lister) / len(list_x))*100), 1 )
def points(list_z):
    list_another = [ ]
    for i in list_z:
        if i >= 0 and i <= 14:
            grade = 0
        elif i >= 15 and i <= 17:
            grade = 1
        elif i >= 18 and i <= 20:
            grade = 2
        elif i >= 21 and i <= 23:
            grade = 3
        elif i >= 24 and i <= 27:
            grade = 4
        elif i >= 28 and i <= 30:
            grade = 5
        list_another.append(grade)
    return list_another
dictionary = { }
list_x = [ ]
list_y = [ ]
list_z = [ ]
while True:
    n = str(input("Exam points and exercises completed: "))
    #exam points 0 - 20 (less than 20 is fail)
    #exercise points 0 - 100 (10% grants 1 point)
    if n == "":
        print ("Statistics:")
        print (f"Points average: {points_exam(list_x, list_y)}")
        print (f"Pass percentage: {pass_pr(list_x)}")
        a = points(list_z).count(5)
        b = points(list_z).count(4)
        c = points(list_z).count(3)
        d = points(list_z).count(2)
        e = points(list_z).count(1)
        f = points(list_z).count(0)
        print ("Grade distribution:")
        print ("5: "+a*"*")
        print ("4: "+b*"*")
        print ("3: "+c*"*")
        print ("2: "+d*"*")
        print ("1: "+e*"*")
        print ("0: "+f*"*")
        break
    else:
        lister = n.split(" ")
        u_1 = lister[0]
        u_2 = lister[1]
        list_x.append(int(u_1)) #list so vsemi examenami
        list_y.append(int(u_2)) #list so vsemi exercisami
        list_z.append(int(u_1)+(int(u_2)/10)) #list s ballami