from random import randint

def roll(die: str):
    if die == "A":
        lister = [3, 3, 3, 3, 3, 6]
    elif die == "B":
        lister = [2, 2, 2, 5, 5, 5]
    elif die == "C":
        lister = [1, 4, 4, 4, 4, 4]
    return(lister[randint(0,5)])
    
def play(die1: str, die2: str, times: int):
    n = 0
    m = 0
    r = 0
    for i in range (0, times):
        chislo_1 = roll(die1)
        chislo_2 = roll(die2)
        if chislo_1 > chislo_2:
            n = n + 1
        elif chislo_1 < chislo_2:
            m = m + 1
        elif chislo_1 == chislo_2:
            r = r + 1
    return (n, m, r)