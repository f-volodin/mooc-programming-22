list=[]
while True:
    n = int(input("New item: "))
    if n==0:
        print("Bye!")
        break
    list.append(n)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")