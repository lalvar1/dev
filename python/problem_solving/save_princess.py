
def display_path_to_princess(n, grid):
    moves = []
    princess_pos = [[grid.index(i), i[0].index('p')] for i in grid if 'p' in i]
    row = princess_pos[0][0]
    col = princess_pos[0][1]
    start_bot_row = start_bot_col = n // 2
    while start_bot_row != row and start_bot_col != col:
        if start_bot_row > row:
            moves.append('UP')
            start_bot_row -= 1
        elif start_bot_row < row:
            moves.append('DOWN')
            start_bot_row += 1
        if start_bot_col > col:
            moves.append('LEFT')
            start_bot_col -= 1
        elif start_bot_col < col:
            moves.append('RIGHT')
            start_bot_col += 1
    print(*moves, sep='\n')

display_path_to_princess(3, ['---', '-m-', 'p--'])
