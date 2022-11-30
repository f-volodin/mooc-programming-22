def distinct_numbers(my_list):
    list2 = sorted(my_list)

    list3 = []
    [list3.append(x) for x in list2 if x not in list3]
    return(list3)