def length_of_longest(my_list):
    n = 0
    for i in my_list:
        if len(i)>n:
            n = len(i)
    return(n)