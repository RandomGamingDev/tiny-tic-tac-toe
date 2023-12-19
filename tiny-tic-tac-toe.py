game = { "board": [[' ' for _ in range(3)] for _ in range(3)], "move": 0 }
[print(f" { game['board'][int(i / 2)][0] } | { game['board'][int(i / 2)][1] } | { game['board'][int(i / 2)][2] } ") if i % 2 == 0 else print("-----------") for i in range(len(game['board']) * 2 - 1)]
while game['move'] < 9:
    x, y = [input(f"Enter the { ['x', 'y'][i] }: ") for i in range(2)]
    if not x.isdigit() or not 1 <= int(x) <= 3 or not y.isdigit() or not 1 <= int(y) <= 3 or game['board'][int(y) - 1][int(x) - 1] != ' ': continue
    game['board'][int(y) - 1][int(x) - 1] = ['X', 'O'][game['move'] % 2]
    [print(f" { game['board'][int(i / 2)][0] } | { game['board'][int(i / 2)][1] } | { game['board'][int(i / 2)][2] } ") if i % 2 == 0 else print("-----------") for i in range(len(game['board']) * 2 - 1)]
    [[quit(f"{ ['X', 'O'][game['move'] % 2] } won!") if row == [['X', 'O'][game['move'] % 2] for _ in range(3)] else None for row in b] for b in [game['board'], [[game['board'][i][j] for i in range(3)] for j in range(3)], [[game['board'][0][0], game['board'][1][1], game['board'][2][2]], [game['board'][2][0], game['board'][1][1], game['board'][0][2]]]]]
    game['move'] += 1
print("Tied!")
