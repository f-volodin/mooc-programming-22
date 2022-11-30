# Write your solution here
def spruce(x):
    n=1
    print("a spruce!")
    while x>n//2:
        print((x-n//2-1)*" "+n*"*")
        n=n+2
    print((x-1)*" "+"*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(-100)
    