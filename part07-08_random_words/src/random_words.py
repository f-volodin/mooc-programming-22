def words(n: int, beginning: str):
    from random import randint
    empty_list = [ ]
    other_list = [ ]
    super_list = [ ]
    u = n
    with open ("words.txt") as my_file:
        for line in my_file:
            empty_list.append(line) 
            #empty list is lis with all words
    for i in empty_list:
        if beginning == i[0:len(beginning)] and i not in other_list:
            other_list.append(i)
        #receivedd other list of which we choose random words
    while n != 0:
        struna = other_list[randint(0, len(other_list)-1)]
        super_list.append(struna)
        n = n - 1
    if u > len(other_list):
        raise ValueError
    
    return (super_list)
    #good job, teper ebash value error pri izbytke







if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
#cat
#car
#carbon