'''
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan
'''
import numpy as np
import time


class Lazor(object):
    '''
    This is the class for Lazor
    '''
    def __init__(self, start, direction):
        '''
        initial the lazor with its origin and direction

        **Parameters**
            start: *tuple, int*
                origin position point.
            direction: *tuple, int*
                diretion of lazor.
        '''
        assert isinstance(start, tuple) and len(start) == 2, \
            "the start of lazors are not applicable"
        assert isinstance(direction, tuple) and len(direction) == 2, \
            "the direction of lazors are not applicable"
        self.start = start
        self.direction = direction

    def goal_search(self, grid, goal):
        '''
        this function tracks the goal points left after crossed by this lazor

        **Parameters**
            grid: *list, list, int*
                grid after putting fixed blocks
            goal: *list, tuple, int*
                list of x,y positions for all the goals

        **Return**
            goal_left: *list, tuple, int*
                goals have not hit by the lazor
        '''
        self.goal = goal
        lazor_path = self.return_block_point_cross(grid)[1]
        goal_left = [i for i in goal if i not in lazor_path]
        return goal_left

    def return_block_point_cross(self, grid):
        '''
        this function returns the blocks and points that lazor crossed

        **Parameters**
            grid: *list, list, string/int*
                grid of the game.

        **Return**
            block_cross: *list, tuple, int*
                list of blocks' position that is crossed by the lazor
            lazor_path: *list, tuple, int*
                list of points' position that is crossed by the lazor
        '''
        cur_point = self.start
        direction = self.direction

        def next_b(cur_point, direction):
            '''
            this function returns the next block's position

            **Parameters**
                cur_point: *tuple, int*
                    current point position of lazor.
                direction: *tuple, int*
                    direction of lazor

            **Return**
                next_b: *tuple, int*
                    next block position
            '''
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
            '''
            this function checks if the next lazor position is still in grid

            **Parameters**
                cur_point: *tuple*
                    current point position of lazor.
                direction: *tuple*
                    direction of lazor

            **Return**
                True/False: *bool*
                    Return True if the next point is in the grid
            '''
            next_x = cur_point[0] + direction[0]
            next_y = cur_point[1] + direction[1]
            if 0 <= next_x < len(grid[0]) \
               and 0 <= next_y < len(grid):
                return True
            else:
                return False

        def reflect(cur_point, direction, next_block):
            '''
            this function returns a new lazor direction after reflection

            **Parameters**
                cur_point: *tuple, int*
                    current point position of lazor.
                direction: *tuple, int*
                    direction of lazor
                next_block: *tuple, int*
                    new block's position

            **Return**
                direction: *tuple, int*
                    new direction after reflect
            '''
            minze = (
                next_block[0] - cur_point[0],
                next_block[1] - cur_point[1]
                )
            direction = (
                direction[0] - 2 * minze[0],
                direction[1] - 2 * minze[1]
                )
            return direction

        # here is the main function script
        block_cross = []
        lazor_path = []
        lazor_path.append(self.start)
        while next_p_check(cur_point, direction):
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
                # start a new lazor along the orgin direction
                lazor_2 = Lazor(new_start, direction)
                lazor_2_block_point = lazor_2.return_block_point_cross(grid)
                # get all the block and point crossed by the new lazor
                for i in lazor_2_block_point[0]:
                    block_cross.append(i)
                for i in lazor_2_block_point[1]:
                    lazor_path.append(i)
                # reflect the current lazor
                direction = reflect(cur_point, direction, next_block)
                continue
            # append block crossed if the block is 'o'
            elif next_block_t == 'o':
                block_cross.append(next_block)

            # update the current point to the next point
            cur_point = (
                cur_point[0] + direction[0],
                cur_point[1] + direction[1]
                )
            lazor_path.append(cur_point)
        return block_cross, lazor_path


def read_puzzle(fptr):
    '''
    this function reads the puzzle from the bff file

    **Parameters**
        fptr: *fptr*
            .bff file that needed to read

    **Return**
        grid: *list, list, int/str*
            grid after putting fixed block
        blocks: *dict*
            keys are the number for certain type of blocks
        lazors: *list, object*
            lists of lazors after initiate
        goal: *list, tuple, int*
            list of x,y positions for all the goal
    '''
    f = open(fptr, 'r')
    f = f.readlines()
    f = [i.replace('\n', '') for i in f if not i == '\n']
    assert 'GRID START' in f and 'GRID STOP' in f, "grid is not readable"

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

    block_sum = sum(blocks[b] for b in blocks)
    assert block_sum != 0, "not block is available to put"
    assert goal != [], "no goal is available in the file"
    assert lazors != [], "no lazors are available in the file"
    return grid, blocks, lazors, goal


def visualize(grid, put_list):
    '''
    this function helps gamer to visualize the result

    **Parameters**
        grid: *list, list, int/string*
            the grid needed to put block
        put_list: *list*
            solved blocks' positions and types
    '''
    assert isinstance(grid, list), "grid is not readable"
    assert isinstance(put_list, list) and len(put_list[0]) == 2, \
        "put_list is not readable"
    f = open("solution.txt", 'w')
    solution = []
    for y in range(1, len(grid), 2):
        for x in grid[y]:
            if x == 0:
                grid[y].remove(x)
        solution.append(' '.join(grid[y]))
    solution = '\n'.join(solution)
    f.write(solution)
    f.close()


def put_block(block_type, block_choice, grid):
    '''
    this function puts the blocks in the grid

    **Parameters**
        block_type: *str*
            type of block, [A, B, C, o, x]
        block_choice: *tuple, int*
            the position of block needed to put
        grid: *list, list, int/str*
            the grid needed to put block

    **Return**
        grid: *list, list, int/str*
            new grid after put blocks
    '''
    total_type = ['x', 'o', 'A', 'B', 'C']
    assert block_type in total_type, "Can't recognize the block type"
    assert isinstance(block_choice, tuple) and len(block_choice) == 2, \
        "please input the right (x, y)"

    (x, y) = block_choice
    grid[y][x] = block_type
    return grid


def check_solve(lazor_list, grid, goal):
    '''
    this function checks goals get solved or not

    **Parameters**
        lazor_list: *list, object*
            original lazors positions
        grid: *list, list, int/str*
            the grid with blocks put
        goal: *list, tuple, int*
            all target points need to be hit by the lazor

    ** Return**
        True/False: *bool*
            True if no goals are unhit
    '''
    for l in lazor_list:
        goal = l.goal_search(grid, goal)
    if goal == []:
        return True
    else:
        return False


def putable_b(grid):
    '''
    this function puts all available blocks on the grid

    **Parameters**
        grid: *list, list, int/str*
            the grid needed to put block

    **Return**
        putable_b: *list, tuple, int*
            positions of all putable blocks
    '''
    putable_b = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'o':
                putable_b.append((x, y))
    return putable_b


def solve_it_by_force(ftpr):
    '''
    this function solves the game by force.
    Here we consider in some cases, not all the functional blocks are used.
    The code search all the posibilities for putting blocks.

    **Parameters**
        fptr: *fptr*
            .bff file that needed to read

    **Return**
        grid: *list, list, int/str*
            new grid after solve the game
        put_list: *list*
            blocks put in the grid
        False: *bool*
            return false if puzzle can't be solved
    '''
    grid, blocks, lazors, goal = read_puzzle(ftpr)
    block_sum = sum(blocks[b] for b in blocks)
    attempt = [{'A': [], 'B': [], 'C': []} for i in range(block_sum)]
    put_list = []

    while len(put_list) <= block_sum:
        b_pos = []
        b_type_pos = []
        putable_bs = putable_b(grid)
        for t in ['A', 'B', 'C']:
            for bs in putable_bs:
                # if there are this type of blocks avaliable and
                # there is postions that haven't tried before
                if blocks[t] != 0 and bs not in attempt[len(put_list)][t]:
                    b_type_pos.append(t)

        if b_type_pos != []:
            b_type_choice = np.random.choice(b_type_pos)
            # find out what position haven't been tried before
            b_pos = [b for b in putable_bs
                     if b not in attempt[len(put_list)][b_type_choice]]
            b_choice = b_pos[np.random.randint(0, len(b_pos))]
            grid = put_block(b_type_choice, b_choice, grid)
            attempt[len(put_list)][b_type_choice].append(b_choice)
            put_list.append((b_choice, b_type_choice))
            blocks[b_type_choice] -= 1

        elif b_type_pos == [] and put_list != []:
            (x, y), t = put_list[-1]
            grid = put_block('o', (x, y), grid)
            blocks[t] += 1
            # if no next step is avaliable while not all blocks are put
            if len(put_list) != block_sum:
                # re-initialize the attempt dict for the last step
                attempt[len(put_list)] = {'A': [], 'B': [], 'C': []}
            put_list.pop()

        # if putlist is empty, no solution can be generated by this code
        elif b_type_pos == [] and put_list == []:
            return False

        if len(put_list) == block_sum:
            solve = check_solve(lazors, grid, goal)
            if solve:
                print("slove grid:", grid)
                print("solve put_list", put_list)
                return grid, put_list
            else:
                continue


def solve_it_smart(ftpr):
    '''
    this function solves the game in a smart way
    The code puts all the funcional block in their functional positions

    **Parameters**
        fptr: *fptr*
            .bff file that needed to read

    **Return**
        grid: *list, list, int/str*
            new grid after solve the game
        put_list: *list*
            blocks put in the grid
        False: *bool*
            return False if the puzzle can't be solved
    '''
    grid, blocks, lazors, goal = read_puzzle(ftpr)
    block_sum = sum(blocks[b] for b in blocks)
    # list of visited position distingushed by block type
    attempt = [{'A': [], 'B': [], 'C': []} for i in range(block_sum)]
    put_list = []

    while len(put_list) <= block_sum:
        # find all the blocks lazors cross
        cross_block = [b for l in lazors for
                       b in l.return_block_point_cross(grid)[0]]

        b_type_pos = []
        for t in ['A', 'C']:
            for bs in cross_block:
                # if the type of block is avaliable and
                # has not tried in certain position before
                if blocks[t] != 0 and bs not in attempt[len(put_list)][t]:
                    b_type_pos.append(t)
        if blocks['B'] != 0:
            b_pos_for_b = []
            putable_bs = putable_b(grid)
            for bs in putable_bs:
                # if there is any position in the grid not tried by B
                if bs not in attempt[len(put_list)]['B']:
                    b_pos_for_b.append(bs)
            if b_pos_for_b != []:
                b_type_pos.append('B')

        if b_type_pos != []:
            b_type_choice = np.random.choice(b_type_pos)
            if b_type_choice != 'B':
                b_pos = [b for b in cross_block
                         if b not in attempt[len(put_list)][b_type_choice]]
                b_choice = b_pos[np.random.randint(0, len(b_pos))]
            elif b_type_choice == 'B':
                b_choice = b_pos_for_b[
                    np.random.randint(0, len(b_pos_for_b))
                    ]

            grid = put_block(b_type_choice, b_choice, grid)
            attempt[len(put_list)][b_type_choice].append(b_choice)
            put_list.append((b_choice, b_type_choice))
            blocks[b_type_choice] -= 1

        # for whatever reason there is no avaliable type of blocks to put
        # undo the last step
        elif b_type_pos == [] and put_list != []:
            (x, y), t = put_list[-1]
            grid = put_block('o', (x, y), grid)
            blocks[t] += 1
            # if no avaliable type happen before all avaliable blocks are put
            if len(put_list) != block_sum:
                # undo the last visit list
                attempt[len(put_list)] = {'A': [], 'B': [], 'C': []}
            put_list.pop()

        # if put_list is empty, it means that
        # no possible solution can be generated by this funciton
        elif b_type_pos == [] and put_list == []:
            return False

        # after all the blocks are put, examine if the puzzle is solved
        if len(put_list) == block_sum:
            solve = check_solve(lazors, grid, goal)
            if solve:
                print("slove grid:", grid)
                print("solve put_list:", put_list)
                return grid, put_list
            else:
                continue


def solve_puzzle():
    '''
    this function solves the game by using smart way first, if it does not work
    use the other way. Also records the time spend

    **Parameters**
        fptr: *fptr*
            .bff file that needed to read
    '''
    t1 = time.time()
    print("Please in put your file name, coated with \" \"")
    puzzle = input()
    solve = solve_it_smart(puzzle)
    if not solve:
        solve = solve_it_by_force(ftpr)
        if not solve:
            print("sorry, this maze cannot be solve")

    if solve:
        grid = visualize(solve[0], solve[1])
        t2 = time.time()
        print("time spent:", str(t2 - t1), 's')


if __name__ == '__main__':
    solve_puzzle()
