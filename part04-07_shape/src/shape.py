def line(x,y):
    if len(y)==1:
        print(f"{x*y}")
    elif len(y)>1:
        print(f"{x*y[0]}")
    elif y=="":
        print(x*"*")

def shape(size_tr, char1, size_sq, char2):
    def triangle(size_tr):
        m=1
        while size_tr>0:
            line(m, char1)
            size_tr=size_tr-1
            m = m+1
    def square(size_sq, char2):
        n=size_sq
        while size_sq>0:
            line(size_tr, char2)
            size_sq=size_sq-1
            
    triangle(size_tr)
    square(size_sq, char2)




# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")