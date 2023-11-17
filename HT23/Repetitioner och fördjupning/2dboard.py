board_width = 7
board_height = 7
board = [[0 for _ in range(board_width)] for _ in range(board_height)]


for row in board:
    print(*row)