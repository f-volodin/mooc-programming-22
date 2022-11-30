def block_correct(sudoku: list, row_no: int, column_no: int):
    def matrix_lister(some_set):
        empty_list = []
        for row in some_set:
            for i in row:
                empty_list.append(i)
        return(empty_list)
    new_sudoku = matrix_lister(sudoku)

    z = row_no*9+column_no+1


    
    block = [new_sudoku[z-1], new_sudoku[z], new_sudoku[z+1],
    new_sudoku[z+8], new_sudoku[z+9], new_sudoku[z+10],
    new_sudoku[z+17], new_sudoku[z+18], new_sudoku[z+19]]

    
    zero_list = []
    for i in block:
        if block.count(i)>1 and i != 0:
            zero_list.append(1)
        else:
            zero_list.append(0)
    if 1 in zero_list:
        return False
    else:
        return True