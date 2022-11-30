def sudoku_grid_correct(sudoku: list):
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
    def column_correct(sudoku: list, column_no: int):
        empty_list = []
        other_list = []
        for i in sudoku:
            empty_list.append(i[column_no])
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
    def block_correct(sudoku: list, row_no: int, column_no: int):
        def matrix_lister(some_set):
            empty_list = []
            for row in some_set:
                for i in row:
                    empty_list.append(i)
            return(empty_list)
        new_sudoku = matrix_lister(sudoku)
        x = row_no*9+column_no+1
        block = [new_sudoku[x-1], new_sudoku[x], new_sudoku[x+1],
        new_sudoku[x+8], new_sudoku[x+9], new_sudoku[x+10],
        new_sudoku[x+17], new_sudoku[x+18], new_sudoku[x+19]]
        super_list = []
        for i in block:
            if block.count(i)>1 and i != 0:
                super_list.append(1)
            else:
                super_list.append(0)
        if 1 in super_list:
            return False
        else:
            return True
    Helper_list = []
    for i in range(0,8):
        if row_correct(sudoku, i) == True:
            Helper_list.append(True)
        else:
            Helper_list.append(False)
    for i in range(0,8):
        if column_correct(sudoku, i) == True:
            Helper_list.append(True)
        else:
            Helper_list.append(False) 
    for m in [0,3,6]:
        for n in [0,3,6]:
            if block_correct(sudoku, m, n) == True:
                Helper_list.append(True)
            else:
                Helper_list.append(False)
    if False in Helper_list:
        return False
    else:
        return True