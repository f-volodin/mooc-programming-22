s1="visual studio code"
s2="word"
s3="notepad"
while True:
    n=str(input("Editor: "))
    if s1==n.lower():
        print("an excellent choice!")
        break
    elif s2==n.lower() or s3==n.lower():
        print("awful")
        continue
    else:
        print("not good")
        continue