board = [[' ' for _ in range(3)] for _ in range(3)]
move = 0
[print(f" { board[int(i / 2)][0] } | { board[int(i / 2)][1] } | { board[int(i / 2)][2] } ") if i % 2 == 0 else print("-----------") for i in range(len(board) * 2 - 1)]
while move < 9:
    x, y = [input(f"Enter the { ['x', 'y'][i] }: ") for i in range(2)]
    if not x.isdigit() or not 1 <= int(x) <= 3 or not y.isdigit() or not 1 <= int(y) <= 3 or board[int(y) - 1][int(x) - 1] != ' ': continue
    board[int(y) - 1][int(x) - 1] = ['X', 'O'][move % 2]
    [print(f" { board[int(i / 2)][0] } | { board[int(i / 2)][1] } | { board[int(i / 2)][2] } ") if i % 2 == 0 else print("-----------") for i in range(len(board) * 2 - 1)]
    [[quit(f"{ ['X', 'O'][move % 2] } won!") if row == [['X', 'O'][move % 2] for _ in range(3)] else None for row in b] for b in [board, [[board[i][j] for i in range(3)] for j in range(3)], [[board[0][0], board[1][1], board[2][2]], [board[2][0], board[1][1], board[0][2]]]]]
    move += 1
print("Tied!")
