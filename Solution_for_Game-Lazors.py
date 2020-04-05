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
        lazor_path = self.return_block_point_cross(grid)[1]
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

        def next_p_check(cur_point, direction):
            next_x = cur_point[0] + direction[0]
            next_y = cur_point[1] + direction[1]
            if 0 <= next_x < len(grid[0]) \
               and 0 <= next_y < len(grid):
                return True
            else:
                return False

        def reflect(cur_point, direction, next_block):
            minze = (
                next_block[0] - cur_point[0],
                next_block[1] - cur_point[1]
                )
            direction = (
                direction[0] - 2 * minze[0],
                direction[1] - 2 * minze[1]
                )
            return direction

        block_cross = []
        lazor_path = []
        lazor_path.append(self.start)
        while next_p_check(cur_point, direction):
            # define next_block to be position + a random block type
            next_block = next_b(cur_point, direction)
            next_block_t = grid[next_block[1]][next_block[0]]
            if next_block_t == 'A':
                direction = reflect(cur_point, direction, next_block)
            elif next_block_t == 'B':
                return block_cross, lazor_path
            elif next_block_t == 'C':
                new_start = (
                    cur_point[0] + direction[0],
                    cur_point[1] + direction[1]
                )
                lazor_2 = Lazor(new_start, direction)
                lazor_2_block_point = lazor_2.return_block_point_cross(grid)
                direction = reflect(cur_point, direction, next_block)
                for i in lazor_2_block_point[0]:
                    block_cross.append(i)
                for i in lazor_2_block_point[1]:
                    lazor_path.append(i)
            elif next_block_t == 'o':
                block_cross.append(next_block)
            # calculate the next point lazor will be
            cur_point = (
                cur_point[0] + direction[0],
                cur_point[1] + direction[1]
                )
            # store all lazor path
            lazor_path.append(cur_point)
        return block_cross, lazor_path


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
            lazor_list.append(
                [tuple(map(int, i.replace('L', '').split()[s:s + 2]))
                 for s in [0, 2]]
                )
        elif i[0] == 'P':
            goal.append(tuple(map(int, i.replace('P', '').split())))
    lazors = [Lazor(l[0], l[1]) for l in lazor_list]
    print(grid_msg)
    print(len(grid))
    print(len(grid[0]))
    # print(blocks)
    print(lazor_list)
    # print("start", lazors[0].start)
    # # print(y)
    print(goal)
    return grid, blocks, lazors, goal


def check_solve(lazor_list, grid, goal):
    for l in lazor_list:
        goal = l.goal_search(grid, goal)
    print(goal)
    if goal == []:
        return True
    else:
        return False


def putable_b(grid):
    pass


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
            cross_block = [b for l in lazors for
                           b in l.return_block_point_cross(grid)[0]]

            # print("find", cross_block)

            b_type_pos = []
            # print("attempt", attempt)
            for t in ['A', 'C']:
                for bs in cross_block:
                    if blocks[t] != 0 and bs not in attempt[len(put_list)][t]:
                        b_type_pos.append(t)
            # if blocks['B'] != 0: # and still places to try to put:
            #     b_type_pos.append('B')

            if b_type_pos == []:
                # print("things to pop", put_list)
                (x, y), t = put_list[-1]
                grid = put_block('o', (x, y), grid)
                blocks[t] += 1
                if len(put_list) != block_sum:
                    attempt[len(put_list)] = {'A': [], 'B': [], 'C': []}
                put_list.pop()

            elif b_type_pos != []:
                b_type_choice = np.random.choice(b_type_pos)
                if b_type_choice != 'B':
                # b_pos = []
                # for b in cross_block:
                #     if b not in attempt[len(put_list)][b_type_choice]:
                #         b_pos.append(b)
                    b_pos = [b for b in cross_block
                             if b not in attempt[len(put_list)][b_type_choice]]
                    rand_choice = np.random.randint(0, len(b_pos))
                    b_choice = b_pos[rand_choice]
                elif b_type_choice == 'B':
                    # just put it somewhere
                    pass

                grid = put_block(b_type_choice, b_choice, grid)
                attempt[len(put_list)][b_type_choice].append(b_choice)
                put_list.append((b_choice, b_type_choice))
                blocks[b_type_choice] -= 1
                # print("after put", put_list)

                solve = check_solve(lazors, grid, goal)
                if solve:
                    print("slove", grid)
                    print("solve", put_list)
                    return grid, put_list


if __name__ == '__main__':
    s = slove_puzzle('template/tiny_5.bff')
