def lottery_numbers(amount: int, lower: int, upper: int):
    from random import randint
    my_list = [ ]
    while amount != 0:
        u = randint(lower, upper)
        if u not in my_list:
            my_list.append(u)
            amount = amount - 1
    my_list = sorted(my_list)
    return(my_list)