def oldest_person(people: list):
    empty_list = [ ]
    for i in people:
        empty_list.append(i[1])
    old = min(empty_list)
    for n in people:
        if old == n[1]:
            return n[0]