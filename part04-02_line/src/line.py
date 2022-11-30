# Write your solution here
def line(x,y):
    if len(y)==1:
        print(f"{x*y}")
    elif len(y)>1:
        print(f"{x*y[0]}")
    elif y=="":
        print(x*"*")
# You can test your function by calling it within the following block
if __name__ == "__main__":  
    line(5,"")