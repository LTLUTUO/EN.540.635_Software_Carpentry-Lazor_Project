# -*- coding: utf-8 -*-
"""
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan

"""


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

    def goal_search(self, goal):
        '''
        this function tracks the goal points left

        **Parameters**
            goal: *tuple*
                   goal points for the game.
        '''
        self.goal = goal
        goal_left = []
        for i in goal:
            if i not in lazor_path:
                goal_left.append(i)
        goal = goal_left
        return goal

    def return_block_point_cross(self, grid):
        '''
        this function tracks the lazor path, store the crossed blocks and points

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
            if next_x % 2, cur_y % 2:
                next_b = (next_x, cur_y)
            if cur_x % 2, next_y % 2:
                next_b = (cur_x, next_y)
            return next_b

        def reflect(cur_point, direction, next_block):
            minze = (next_block[0] - cur_point[0], next_block[1] - cur_point[1])
            direction = (direction[0] - 2 * minze[0], direction[1] - 2 * minze[1])
            return direction

        block_cross = []
        lazor_path = []
        lazor_path.append(self.start)
        while lazor in grid:

            # define next_block to be position + a random block type
            next_block = next_b(next_point, direction)
            next_block_t = grid[next_block[0]][next_block[1]]
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
            next_point = [cur_point[0] + direction[0],
                          cur_point[1] + direction[1]]
            # store all lazor path
            lazor_path.append(lazor_next)
        return [block_cross, lazor_path]
