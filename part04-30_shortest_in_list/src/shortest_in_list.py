def shortest(my_list):
    n = 10000000000
    for i in my_list:
        if len(i)<n:
            n = len(i)
            word = i
    return(word)
    