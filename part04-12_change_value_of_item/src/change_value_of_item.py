list = [1, 2, 3, 4, 5]
n=0
while True:
    n = int(input("Index: "))
    if n==-1:
        break
    m = int(input("New value: "))
    list[n]=m
    print(list)