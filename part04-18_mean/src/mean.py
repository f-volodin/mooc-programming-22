# Write your solution here

def mean(my_list):
    n = sum(my_list)
    m = len(my_list)
    u = n/m
    return u

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)