def most_common_character (string):
    max_frequency = {}
    for i in string:
        if i in max_frequency:
            max_frequency[i] = max_frequency[i] + 1
        else:
            max_frequency[i] = 1
    result = max(max_frequency, key = max_frequency.get)
    return(result)