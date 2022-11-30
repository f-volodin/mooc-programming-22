def is_it_valid(pic: str):
#midsummer = datetime(2021, 6, 26)
    try:
    
        if len(pic) != 11:
            return False
        check_2 = pic[6]
        check_1 = pic[0:6]
        from datetime import datetime
        if check_2 =="-":
            birth = datetime(int(check_1[4:6])+1900, int(check_1[2:4]), int(check_1[0:2]))
        elif check_2 == "+":
            birth = datetime(int(check_1[4:6])+1800, int(check_1[2:4]), int(check_1[0:2]))
        elif check_2 == "A":
             birth = datetime(int(check_1[4:6])+2000, int(check_1[2:4]), int(check_1[0:2]))
        else:
        #print("bastard")
            return False
        
    except ValueError:
        return False
    
    control = (pic[7:10])
    m = str(check_1) + control
    n = (int(m) % 31)
    #n is remainder
    struna = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if struna[n] != pic[10]:
        return False
    else:
        return True
    