def who_won(game_board: list):
    empty_list = []
    for row in game_board:
        for i in row:
            empty_list.append(i)
    n_1 = empty_list.count(1)
    n_2 = empty_list.count(2)
    n_0 = empty_list.count(0)
    if n_1 > n_2:
        return(1)
    elif n_2 > n_1:
        return(2)
    else:
        return(0)