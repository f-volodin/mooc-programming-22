def generate_password(length):
    from random import randint
    struna = ""
    alef = "abcdefghijklmnopqrstuvwxyz"
    while len(struna) < length:
        struna = struna + (alef[randint(0, 25)])
    return(struna)