n = str(input("Whom should I sign this to: "))
x_file = str(input("Where shall I save it: "))
with open (x_file , "w") as my_file:
    my_file.write(f"Hi {n}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

print (my_file)