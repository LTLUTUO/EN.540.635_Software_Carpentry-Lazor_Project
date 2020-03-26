'''
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan
'''
import numpy as np


#def put Block(block_id, xy):
    # init
    # putblock
    # readblock
    # pass


# class Lazor(self, point_direction):
    # init
    # start lazor
    #   readblock
    #   gotonext readblock
    #   return all the point crossed
    # # crossed_block
    # #  return all block crossed
    # def check_solve(self, goal):
    #     for i in goal:
    #         if i not in crossed:
    #             return False
    #     return True
    # pass


def read_puzzle(fptr):
    f = open(fptr, 'r')
    f = f.readlines()
    print(f)
    f = [i.replace('\n', '') for i in f if not i == '\n']

    # grid is the slice of list from start to stop
    grid_msg = [i.replace(' ', '')
                for i in f[f.index('GRID START') + 1:f.index('GRID STOP')]]
    grid = [[0 for i in range(len(grid_msg[0]) * 2 + 1)]
            for i in range(len(grid_msg) * 2 + 1)]
    for i in grid_msg:
        for b in i:
            # putblocks
            pass

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
    return grid, blocks, lazors, goal


# def slove_puzzle(ftpr):
#     grid, blocks, lazors, goal = read_puzzle()
#     attempt = []
#     lazors = lazor(lazors)
#     solve = lazors.check_solve(goal)
#     while not solve:
#         cross_block = lazors.cross_block()
#         for poss_block in cross_block:
#             # random select block type
#             # put block
#             # append position
#             pass


read_puzzle('template/numbered_6 copy.bff')
