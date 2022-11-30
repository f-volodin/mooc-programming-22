def count_matching_elements(my_matrix: list, element: int):
    empty_list = []
    for row in my_matrix:
        for i in row:
            empty_list.append(i)
    return(empty_list.count(element))