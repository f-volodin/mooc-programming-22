def fractionate(amount: int):
    from fractions import Fraction
    list_x = [ ]
    for n in range(0, amount):
        u = Fraction(1, amount)
        list_x.append(u)
    return(list_x)