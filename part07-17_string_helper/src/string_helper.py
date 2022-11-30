def change_case(orig_string: str):
    orig_string = orig_string.swapcase()
    return (orig_string)

def split_in_half(orig_string: str):
    tuple_x = ( orig_string[0:len(orig_string)//2] , orig_string[len(orig_string)//2:len(orig_string)])
    return (tuple_x)

def remove_special_characters(orig_string: str):
    n = 0
    struna = "QWERTYUIOPASDFGHJKLZXCVBNM 1234567890qwertyuiopasdfghjklzxcvbnm"
    while n != len(orig_string):
        if orig_string[n] not in struna:
            orig_string = orig_string.replace(orig_string[n] , "#")
        n = n + 1
    orig_string = orig_string.replace("#" , "")
    return(orig_string)