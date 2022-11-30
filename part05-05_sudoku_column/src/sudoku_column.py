def column_correct(sudoku: list, column_no: int):
    empty_list = []
    other_list = []
    for i in sudoku:
        empty_list.append(i[column_no])
    #poluchili empty_list - set s kolonnoj
    for number in empty_list:
        r = empty_list.count(number)
        if number != 0 and r > 1:
            other_list.append(0)
        else:
            other_list.append(1)
    if 0 in other_list:
        return False
    else:
        return True