def formatted(my_list):
    new_list = []
    for i in my_list:
        n=f"{i:.2f}"
        new_list.append(n)
    return(new_list)