# Write your solution here


def same_chars(string, x, y):
    if len(string)>y and len(string)>x:
        if string[x]==string[y]:
            return True
        else:
            return False
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))