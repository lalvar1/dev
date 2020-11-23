
grid = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
pattern = ['9505', '3845', '3530']
grid2 = ['34889246430321978567', '58957542800420926643', '35502505614464308821', '14858224623252492823', '72509980920257761017', '22842014894387119401', '01112950562348692493', '16417403478999610594', '79426411112116726706', '65175742483779283052', '89078730337964397201', '13765228547239925167', '26113704444636815161', '25993216162800952044', '88796416233981756034', '14416627212117283516', '15248825304941012863', '88460496662793369385', '59727291023618867708', '19755940017808628326']
pattern2 = ['1641', '7942', '6517', '8907', '1376', '2691', '2599']
grid3 = ['123456', '567890', '234567', '194729']
pattern3 = ['1234', '5678', '2345', '4729']
# return yes if 2D pattern of digits exists in grid


def grid_search(grid, pattern):
    p_len = len(pattern[0])
    for i, row in enumerate(grid):
        if pattern[0] in row:
            next_indexes = i + 1
            for i, item in enumerate(pattern[1:], 1):
                if item not in grid[next_indexes]:
                    ret = 'NO'
                    break
                p_index = grid[next_indexes].index(item)
                if grid[next_indexes - 1][p_index:p_index + p_len] == pattern[i - 1]:
                    next_indexes += 1
                    ret = 'YES'
                else:
                    ret = 'NO'
                    break
            if ret == 'YES':
                return ret
    return ret


print(grid_search(grid, pattern))

# map(lambda x: True if x in pattern else False, grid[4:])