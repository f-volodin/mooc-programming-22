def factorials(n: int):
    dictionary = { }
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        dictionary[i] = fact
    return(dictionary)