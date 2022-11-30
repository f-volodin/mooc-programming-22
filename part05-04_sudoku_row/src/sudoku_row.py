def row_correct(sudoku: list, row_no: int):
    n = sudoku[row_no]
    empty_list = []
    for i in n:
        r = n.count(i)
        if i != 0 and r > 1:
            empty_list.append(0)
        else:
            empty_list.append(1)
    if 0 in empty_list:
        return False
    else:
        return True