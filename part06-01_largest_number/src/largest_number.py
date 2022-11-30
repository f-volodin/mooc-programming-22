def largest():
    sett = [ ]
    with open("numbers.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            sett.append(int(line))
    n = max(sett)
    return n