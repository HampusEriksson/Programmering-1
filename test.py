board = [["x" for _ in range(10)] for _ in range(10)]

print(board)

for row in board:
    print(*row)

board[0][0] = "O"

for row in board:
    print(*row)