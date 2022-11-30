def no_shouting(lst):
    for item in lst:
        if item.isupper():
            lst.remove(item)
    for item in lst:
        if item.isupper():
            lst.remove(item)
    for item in lst:
        if item.isupper():
            lst.remove(item)
            
    return(lst)