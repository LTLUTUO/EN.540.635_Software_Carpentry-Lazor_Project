'''
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan
'''
import numpy as np


def put_block(block_type, block_pos, grid):
    '''
    this function puts the blocks in the grid

    **Parameters**
        block_type: *str*
            type of block, [A, B, C, o, x]
        block_pos: *tuple, int*
            the position of block needed to put
        grid: *list, list*
            the grid needed to put block
    **Return**
        grid: *list, list*
            new grid after putting block
    '''
    x, y = block_pos
    # print((x, y))
    grid[y][x] = block_type
    # print(grid)
    return grid


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
    '''
    this function puts the blocks in the grid

    **Parameters**
        fptr: *fptr*
            .bff file that needed to read

    **Return**
        grid: *list, list*
            new grid after putting fixed block
        blocks: *dict*
            keys are the number for certain type of blocks
        lazors: *list, list, tuple*
            lists of two tuples, representing starting point and direction
        goal: *list, tuple*
            list of x,y positions for all the goal
    '''
    f = open(fptr, 'r')
    f = f.readlines()
    f = [i.replace('\n', '') for i in f if not i == '\n']

    # grid is the slice of list from start to stop
    grid_msg = [i.replace(' ', '')
                for i in f[f.index('GRID START') + 1:f.index('GRID STOP')]]
    grid = [[0 for i in range(len(grid_msg[0]) * 2 + 1)]
            for i in range(len(grid_msg) * 2 + 1)]
    y = 1
    for i in grid_msg:
        x = 1
        for b in i:
            grid = put_block(b, (x, y), grid)
            x += 2
        y = y + 2

    blocks = {}
    lazors = []
    goal = []
    for i in f[f.index('GRID STOP'):]:
        if i[0] in ['A', 'B', 'C']:
            blocks[i[0]] = int(i[2])
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


def slove_puzzle(ftpr):
    # def get_b_type(blocks):
    #     block = ('A', 'B', 'C')
    #     b_type = [block[i] for i in blocks if blocks[i] != 0]
    #     return b_type

    grid, blocks, lazors, goal = read_puzzle()
    block_sum = sum(blocks[b] for b in blocks)
    attempt = [{'A': [], 'B': [], 'C': []} for i in range(block_sum)]
    put_list = []

    # list of positions that have tried
    # c_blocks = blocks
    lazors = Lazor(lazors) # what if there is multiple lazor
    solve = lazors.check_solve(goal) # multiple check
    while not solve:
        while len(put_list) != block_num:
            cross_block = lazors.cross_block()
            b_type_pos = []
            for t in ['A', 'B', 'C']:
                for b in cross_block:
                    if blocks[t] != 0 and b not in attempt[len(put_list)][t]:
                        b_type_pos.append(t)

            if b_type_pos == []:
                attempt[len(put_list)][b_type_choice] = {
                    'A': [],
                    'B': [],
                    'C': []
                }
                x, y = put_list[-1]
                blocks[grid[y][x]] += 1
                grid = put_block('o', (x, y), grid)
                put_list.pop()
                break

            b_type_choice = np.random.choice(b_type_pos)
            b_pos = [b for b in cross_block
                     if b not in attempt[len(put_list)][b_type_choice]]

            b_choice = np.random.choice(b_pos)

            grid = put_block(b_type_choice, b_choice, grid)
            attempt[len(put_list)][b_type_choice].append(b_choice)
            put_list.append(b_pos)
            blocks[b_type_choice] -= 1

            solve = lazors.check_solve(goal)
            if solve:
                break

        if len(put_list) == block_num:
            attempt[len(put_list)] = []
            x, y = put_list[-1]
            blocks[grid[y][x]] += 1
            grid = put_block('o', (x, y), grid)
            put_list.pop()


                # random select block type
                # put block
                # append position


if __name__ == '__main__':
    blocks = {'a': 5, 'b': 0, 'c': 2}
    b = []
    # b = ['a', 'd']
    # b_type = []
    # blockt = ('a', 'b', 'c')
    # print(a)
    # for i in [a, b, c]:
    #     if i != 0:
    #         b_type.append(i)
    # b_type = [blockt[i] for i in blocks if blocks[i] != 0]
    # print(b_type)
    # e = np.random.choice(b_type)
    # e = sum(blocks[i] for i in blocks)
    # e = [i for i in ['a', 'b', 'c'] if blocks[i] != 0 and i not in b]
    # print(e)
    # read_puzzle('template/numbered_6.bff')
    e = np.random.choice(b)
    print(e)
