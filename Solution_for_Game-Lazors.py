'''
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan
'''
import numpy as np


# def put Block(block_id, xy):
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
            # putblocks(grid_msg[i][b], (i, b))
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


def slove_puzzle(ftpr):
    def get_b_type(blocks):
        block = ('A', 'B', 'C')
        b_type = [block[i] for i in blocks if blocks[i] != 0]
        return b_type

    grid, blocks, lazors, goal = read_puzzle()
    block_sum = sum(b for b in blocks)
    block_num = block_sum
    attempt = [[] for i in range(block_sum)]
    put_list = []
    # c_blocks = blocks
    lazors = Lazor(lazors) # what if there is multiple lazor
    solve = lazors.check_solve(goal) # multiple check
    while not solve:
        cross_block = lazors.cross_block()
        while block_num != 0 and cross_block:
            b_pos = np.random.choice(cross_block)
            b_type = get_b_type(c_blocks)
            b = np.random.choice(b_type)
            if b not in attempt[block_sum - block_num]:
                grid = put_block(b, b_pos, grid)
                put_list.append(b_pos)
                attempt[block_sum - block_num].append(b)
            solve = lazors.check_solve(goal)
            cross_block = lazors.cross_block()
            block_num -= 1
            if solve:
                return "answer"
        if block_num != 0 and not cross_block:
            b_pos = put_list[-1]
            grid = put_block('o', b_pos, grid)
            put_list.pop()
            block_num += 1
        if block_num == 0:
            b_pos = put_list[-1]
            grid = put_block('o', b_pos, grid)
            block_num += 1
            put_list.pop()


                # random select block type
                # put block
                # append position
                pass


if __name__ == '__main__':
    blocks = [1, 0, 2]
    # b_type = []
    blockt = ('a', 'b', 'c')
    # print(a)
    # for i in [a, b, c]:
    #     if i != 0:
    #         b_type.append(i)
    b_type = [blockt[i] for i in blocks if blocks[i] != 0]
    print(b_type)
    e = np.random.choice(b_type)
    print(e)
