list = []
do = ""
n = 1
while True:
    print(f"The list is now", list)
    do = str(input("a(d)d, (r)emove or e(x)it: "))
    if do=="d":
        list.append(n)
        n=n+1
    elif do=="r":
        list.remove(n-1)
        n=n-1
    elif do=="x":
        print("Bye!")
        break
    else:
        continue