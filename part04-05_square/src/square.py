def line(x,y):
    if len(y)==1:
        print(f"{x*y}")
    elif len(y)>1:
        print(f"{x*y[0]}")
    elif y=="":
        print(x*"*")

def square(size, character):
    n=size
    while size>0:
        line(n, character)
        size=size-1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")