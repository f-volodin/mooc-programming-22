def range_of_list(my_list):
    n = max(my_list)
    m = min(my_list)
    r = n - m
    return r

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)