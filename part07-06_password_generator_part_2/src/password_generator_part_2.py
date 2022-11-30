def generate_strong_password(length : int, numbers : bool, specs : bool):
    bukvy = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    chisla = ["1","2","3","4","5","6","7","8","9","0"]
    znaki = ["!","?","=","+","-","(",")","#"]
    alef = "abcdefghijklmnopqrstuvwxyz"
    from random import randint
    struna = ""
    while len(struna) < length-2:
        struna = struna + (alef[randint(0, 25)])
    if numbers == True and specs == True:
        struna = struna + chisla[randint(0,9)]
        struna = struna + znaki[randint(0,7)]
    elif numbers == False and specs == True:
        struna = struna + znaki[randint(0,7)]
        struna = struna + znaki[randint(0,7)]
    elif numbers == True and specs == False:
        struna = struna + chisla[randint(0,9)]
        struna = struna + chisla[randint(0,9)]
    else:
        struna = struna + bukvy[randint(0,25)]
        struna = struna + bukvy[randint(0,25)]
    return(struna)