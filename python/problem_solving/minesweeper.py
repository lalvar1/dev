#One of the coding questions was to generate a minesweeper grid (2x3) with 3 randomly-placed mines.
import random


def method1():
    high_len = 2
    wide_len = 3
    high = []
    wide = []
    for _ in range(high_len):
        for _ in range(wide_len):
            wide.append(random.randint(1, 10))
        wide[random.randint(0, wide_len-1)] = '*'
        high.append(wide)
        wide = []
    high[random.randint(0, high_len-1)][random.randint(0, wide_len-1)] = '*'
    print(*high, sep='\n')


def method2(high_len, wide_len, mines_num):
    # high = [[random.randint(1, 10) for _ in range(wide_len)] for _ in range(high_len)]
    high = [['O' for _ in range(wide_len)] for _ in range(high_len)]
    # for _ in range(mines_num):
    while sum([x.count('*') for x in high]) < mines_num:
        high[random.randint(0, high_len - 1)][random.randint(0, wide_len - 1)] = '*'
    print(*high, sep='\n')


method2(3, 4, 5)



print('------------------')
width=4
height=3
mines= 5
grid = [['O' for _ in range(width)] for _ in range(height)]
while sum([x.count('*') for x in grid]) < mines:
    grid[random.randint(0,height-1)][random.randint(0,width-1)] = '*'

print(*grid, sep='\n')


