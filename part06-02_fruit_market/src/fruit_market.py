def read_fruits():
    dic = { }
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            dic[parts[0]] = float(parts[1])
    return dic
