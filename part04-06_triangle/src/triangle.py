def line(x,y):
    if len(y)==1:
        print(f"{x*y}")
    elif len(y)>1:
        print(f"{x*y[0]}")
    elif y=="":
        print(x*"*")

def triangle(size):
    n=1
    while size>0:
        line(n, "#")
        size=size-1
        n = n+1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
