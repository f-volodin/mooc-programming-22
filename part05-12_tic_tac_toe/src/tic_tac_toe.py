def play_turn(game_board: list, x: int, y: int, piece: str):
    if y > 2 or y < 0:
        return False
    if x > 2 or x < 0:
        return False
    u_helper = game_board[y]
    if u_helper[x] == "":
        u_helper[x] = piece
        game_board[y] = u_helper
        return True
    else:
        return False