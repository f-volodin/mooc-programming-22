def older_people(people: list, year: int):
    empty_list = [ ]
    other_list = [ ]
    another_list = [ ]
    for i in people:
        empty_list.append(i)
        #print(empty_list)
    for i in empty_list:
        if i[1] < year:
            other_list.append(i)
            #print(other_list)
    for i in other_list:
        another_list.append(i[0])
        #print(another_list)
    return another_list