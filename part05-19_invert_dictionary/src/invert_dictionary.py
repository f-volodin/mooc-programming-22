def invert(dictionary: dict):
    list_1 = []
    list_2 = []
    for i in dictionary:
        list_1.append(i)
    for i in dictionary:
        list_2.append(dictionary[i])
    dic = { }
    n = 0
    while n < len(dictionary):
        dic[list_2[n]] = list_1[n]
        n = n + 1
    dictionary.clear()
    dictionary.update(dic)