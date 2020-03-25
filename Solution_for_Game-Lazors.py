'''
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan
'''
import numpy as np


class Block(self, block_id):
    # init
    # putblock
    # readblock
    pass


class Lazor(self, point_direction):
    # init
    # start lazor
    #   readblock
    #   gotonext readblock
    #   return all the point crossed
    pass


def read_maze(fptr):
    f = open(fptr, 'r')
    f = f.readlines()
    f = [i.replace('\n', '') for i in f if not i == '\n']

    # grid is the slice of list from start to stop
    grid_msg = [i.replace(' ', '')
                for i in f[f.index('GRID START') + 1:f.index('GRID STOP')]]
    grid = [[0 for i in range(len(grid_msg[0]) * 2 + 1)]
            for i in range(len(grid_msg) * 2 + 1)]
    for i in grid_msg:
        for b in i:
            # putblocks

    blocks = [0, 0, 0]
    block_type = ['A', 'B', 'C']
    lazors = []
    goal = []
    for i in f:
        if i[0] in block_type:
            blocks[block_type.index(i[0])] = int(i[2])
        elif i[0] == 'L':
            lazors.append([tuple(map(int, i.replace('L', '').split()[s:s + 2]))
                           for s in [0, 2]])
        elif i[0] == 'P':
            goal.append(tuple(map(int, i.replace('P', '').split())))
    print(grid_msg)
    print(grid)
    print(blocks)
    print(lazors)
    print(goal)
    return [grid, blocks, lazors, goal]


def slove_puzzle(ftpr):
    pass


read_maze('template/numbered_6 copy.bff')
