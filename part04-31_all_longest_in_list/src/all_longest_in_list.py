def all_the_longest(my_list):
    n = 0
    list2=[]
    list3=[]
    for i in my_list:
        if len(i)>=n:
            n = len(i)
            word = i
            list2.append(word)
    for i in list2:
        if len(i)>=n:
            n = len(i)
            word = i
            list3.append(word)
    return(list3)