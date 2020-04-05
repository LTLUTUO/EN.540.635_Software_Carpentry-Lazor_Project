'''
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan
'''
import numpy as np


class Lazor(object):
    '''
    This is the class for Lazor
    '''
    def __init__(self, start, direction):
        '''
        initial the lazor with its origin and direction
        **Parameters**
            start: *tuple*
                   origin position point.
            direction: *tuple*
                      diretion of lazor.
        '''
        self.start = start
        self.direction = direction

    def goal_search(self, grid, goal):
        '''
        this function tracks the goal points left

        **Parameters**
            goal_left: *tuple*
                   goal points for the game.
        '''
        self.goal = goal
        self.grid = grid
        lazor_path = self.return_block_point_cross(self.grid)[1]
        goal_left = [i for i in goal if i not in lazor_path]
        return goal_left

    def return_block_point_cross(self, grid):
        '''
        this function return the blocks and points that lazor crosses

        **Parameters**
            grid: *tuple*
                    grid of the game.
        '''
        self.grid = grid
        cur_point = self.start
        direction = self.direction

        def next_b(cur_point, direction):
            cur_x, cur_y = cur_point
            next_x = cur_point[0] + direction[0]
            next_y = cur_point[1] + direction[1]
            if next_x % 2 and cur_y % 2:
                next_b = (next_x, cur_y)
            elif cur_x % 2 and next_y % 2:
                next_b = (cur_x, next_y)
            else:
                return False
            return next_b

        def reflect(cur_point, direction, next_block):
            minze = (next_block[0] - cur_point[0], next_block[1] - cur_point[1])
            direction = (direction[0] - 2 * minze[0], direction[1] - 2 * minze[1])
            return direction

        block_cross = []
        lazor_path = []
        lazor_path.append(self.start)
        while 0 < cur_point[0] < len(grid[0]) and 0 < cur_point[1] < len(grid):
            # define next_block to be position + a random block type
            next_block = next_b(cur_point, direction)
            next_block_t = grid[next_block[1]][next_block[0]]
            if next_block_t == 'A':
                direction = reflect(cur_point, direction, next_block)
            elif next_block_t == 'B':
                return lazor_path
            elif next_block_t == 'C':
                lazor_2 = Lazor(cur_point, direction)
                lazor_2_block_point = lazor_2.return_block_point_cross(grid)
                direction = reflect(cur_point, direction, next_block)
                for i in lazor_2_block_point:
                    block_cross.append(i[0])
                    lazor_path.append(i[1])
            elif next_block_t == 'o':
                block_cross.append(next_block)
            # calculate the next point lazor will be
            cur_point = (cur_point[0] + direction[0], cur_point[1] + direction[1])
            # store all lazor path
            lazor_path.append(cur_point)
        return [block_cross, lazor_path]


def put_block(block_type, block_choice, grid):
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
    (x, y) = block_choice
    grid[y][x] = block_type
    return grid


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

    blocks = {'A': 0, 'B': 0, 'C': 0}
    lazor_list = []
    lazors = []
    goal = []
    for i in f[f.index('GRID STOP'):]:
        if i[0] in ['A', 'B', 'C']:
            blocks[i[0]] = int(i[2])
        elif i[0] == 'L':
            lazor_list.append([tuple(map(int, i.replace('L', '').split()[s:s + 2]))
                               for s in [0, 2]])
        elif i[0] == 'P':
            goal.append(tuple(map(int, i.replace('P', '').split())))
    lazors = [Lazor(l[0], l[1]) for l in lazor_list]
    print(grid_msg)
    print(grid)
    print(blocks)
    print(lazor_list)
    print(lazors[0])
    # print(y)
    print(goal)
    return grid, blocks, lazors, goal


def check_solve(lazor_list, grid, goal):
    for l in lazor_list:
        goal = l.goal_search(grid, goal)
    if goal == []:
        return True
    else:
        return False


def slove_puzzle(ftpr):
    '''
    something here
    '''
    grid, blocks, lazors, goal = read_puzzle(ftpr)
    block_sum = sum(blocks[b] for b in blocks)
    attempt = [{'A': [], 'B': [], 'C': []} for i in range(block_sum)]
    put_list = []

    solve = check_solve(lazors, grid, goal)
    while not solve:
        while len(put_list) <= block_sum:
            cross_block = [b for l in lazors
                           for b in l.return_block_point_cross(grid)[0]]
            # for l in lazors:
            #     c_block = l.return_block_point_cross(grid)[0]
            #     for b in c_block:
            #         cross_block.append(b)
            b_type_pos = []
            for t in ['A', 'B', 'C']:
                for b in cross_block:
                    if blocks[t] != 0 and b not in attempt[len(put_list)][t]:
                        b_type_pos.append(t)

            if b_type_pos == []:
                for t in ['A', 'B', 'C']:
                    attempt[len(put_list)][t] = []
                #     'A': [],
                #     'B': [],
                #     'C': []
                # }
                (x, y), t = put_list[-1]
                blocks[t] += 1
                grid = put_block('o', (x, y), grid)
                put_list.pop()
                break

            b_type_choice = np.random.choice(b_type_pos)
            b_pos = [b for b in cross_block
                     if b not in attempt[len(put_list)][b_type_choice]]
            rand_choice = np.random.randint(0, len(b_pos))
            b_choice = b_pos[rand_choice]
            print(b_pos)
            print(type(b_choice))
            print(type(b_choice[0]))
            print(b_choice)

            grid = put_block(b_type_choice, b_choice, grid)
            attempt[len(put_list)][b_type_choice].append(b_choice)
            put_list.append((b_choice, b_type_choice))
            blocks[b_type_choice] -= 1

            solve = check_solve(lazors, grid, goal)
            if solve:
                print(grid)
                print(put_list)
                return grid, put_list


if __name__ == '__main__':
    # blocks = {'a': 5, 'b': 0, 'c': 2}
    # b = [(1, 2), (3, 4)]
    # e = np.random.choice(b)
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
    s = slove_puzzle('template/mad_4.bff')
    print(s)
    # e = np.random.choice(b)
    # print(e)
