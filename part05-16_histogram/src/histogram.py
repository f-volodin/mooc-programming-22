def histogram(string):
    dic = { }
    n = 0
    for n in range(len(string)):
        if string[n] not in dic:
            dic[string[n]] = string.count(string[n])*"*"
            print(string[n], end='')
            print("", dic[string[n]])
        n = n + 1