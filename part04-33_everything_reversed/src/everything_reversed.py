def everything_reversed(lst):
    empty_list = []
    for i in lst:
        r = i[::-1]
        empty_list.append(r)
    new_empty_list=empty_list[::-1]
    return(new_empty_list)