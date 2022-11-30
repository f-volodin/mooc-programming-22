def times_ten(start_index: int, end_index: int):
    dictionary = { }
    n = start_index
    dictionary[start_index] = start_index*10
    while n != end_index:
        dictionary[n] = n*10
        n = n + 1
    dictionary[end_index] = end_index*10
    return(dictionary)