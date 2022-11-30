import string
def separate_characters(my_string):
    struna_1 = ""
    struna_2 = ""
    struna_3 = ""
    for i in my_string:
        if i in string.ascii_letters:
            struna_1 = struna_1+i
    for i in my_string:
        if i in string.punctuation:
            struna_2 = struna_2+i        
    for i in my_string:
        if i not in string.punctuation and i not in string.ascii_letters:
            struna_3 = struna_3+i        
    touple = (struna_1, struna_2, struna_3)
    return (touple)