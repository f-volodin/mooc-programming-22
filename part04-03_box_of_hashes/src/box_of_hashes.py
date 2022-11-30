def line(x,y):
    if len(y)==1:
        print(f"{x*y}")
    elif len(y)>1:
        print(f"{x*y[0]}")
    elif y=="":
        print(x*"*")

def box_of_hashes(height):
    while height>0:
        line(10, "#")
        height=height-1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
