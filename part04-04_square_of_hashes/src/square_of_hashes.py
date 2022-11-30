def line(x,y):
    if len(y)==1:
        print(f"{x*y}")
    elif len(y)>1:
        print(f"{x*y[0]}")
    elif y=="":
        print(x*"*")

def square_of_hashes(size):
    n=size
    while size>0:
        line(n, "#")
        size=size-1



# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
