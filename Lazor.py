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
    
    def return_block_point_cross(self, grid):
        '''
        this function tracks the lazor path, store the crossed blocks and points
        
        **Parameters**
            grid: *tuple*
                   grid of the game.       
        
        '''
        self.grid = grid

        # assign lazor at starting position
        lazor = start
        block_corss = []
        block_position = []
        block_intercept = {(block_position[0], block_position[1] - 1): 'top', (block_position[0], block_position[1] + 1): 'bot',
                           (block_position[0] - 1, block_position[1]): 'left', (block_position[0] + 1, block_position[1]): 'right',}
        function_block = ['A', 'B', 'C']
        lazor_path = [start]
        possible_directions = [[1, -1], [-1, -1], [-1, 1], [1, 1]]
        while lazor in grid:
            # calculate the next point lazor will be
            lazor_next = [start[0] + direction[0], start[1] + direction [1]]
            # store all lazor path
            lazor_path = [lazor_path, lazor_next]
            # define next_block to be position + a random block type
            block_type = random.choice('OXABC')
            next_block = [block_position, block_type]
            if next_block[1:] in funciton_block:
                if next_block[1:] == 'A':
                    # reflect block, change lazor direction
                    if direction is [1, -1]:
                        # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'left':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] - 1]
                        elif lazor_next == 'bot':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] + 1]
                        elif lazor_next == 'right' or lazor_next == 'top':
                            lazor_next = [lazor_next[0] - 2, lazor_next[1] + 2]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                    elif direction is [-1, -1]:
                         # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'right':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] - 1]
                        elif lazor_next == 'bot':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] + 1]
                        elif lazor_next == 'left' or lazor_next == 'top':
                            lazor_next = [lazor_next[0] + 2, lazor_next[1] + 2]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                    elif direction is [-1, 1]:
                        # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'right':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] + 1]
                        elif lazor_next == 'top':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] - 1]
                        elif lazor_next == 'left' or lazor_next == 'bot':
                            lazor_next = [lazor_next[0] + 2, lazor_next[1] - 2]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                    elif direction is [1, 1]:
                        # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'left':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] + 1]
                        elif lazor_next == 'top':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] - 1]
                        elif lazor_next == 'right' or lazor_next == 'bot':
                            lazor_next = [lazor_next[0] - 2, lazor_next[1] - 2]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
               
                elif next_block[1:] == 'C':
                    # refract block, reulting two lazor path
                    if direction is [1, -1]:
                        # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'left':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] - 1]
                            lazor_next2 = [lazor_next[0] + 1, lazor_next[1] - 1]
                        elif lazor_next == 'bot':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] - 1]
                            lazor_next2 = [lazor_next[0] + 1, lazor_next[1] - 1]
                        elif lazor_next == 'right' or lazor_next == 'top':
                            lazor_next = [lazor_next[0] - 2, lazor_next[1] + 2]
                            lazor_next2 = [lazor_next[0] + 1, lazor_next[1] - 1]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                        lazor_path.append(lazor_next2)
                    elif direction is [-1, -1]:
                         # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'right':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] - 1]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] - 1]
                        elif lazor_next == 'bot':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] + 1]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] - 1]
                        elif lazor_next == 'left' or lazor_next == 'top':
                            lazor_next = [lazor_next[0] + 2, lazor_next[1] + 2]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] - 1]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                        lazor_path.append(lazor_next2)     
                    elif direction is [-1, 1]:
                         # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'right':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] + 1]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] + 1]
                        elif lazor_next == 'top':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] - 1]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] + 1]
                        elif lazor_next == 'left' or lazor_next == 'bot':
                            lazor_next = [lazor_next[0] + 2, lazor_next[1] - 2]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] + 1]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                        lazor_path.append(lazor_next2)   
                    elif direction is [-1, -1]:
                        # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'right':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] - 1]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] - 1]
                        elif lazor_next == 'bot':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] + 1]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] - 1]
                        elif lazor_next == 'left' or lazor_next == 'top':
                            lazor_next = [lazor_next[0] + 2, lazor_next[1] + 2]
                            lazor_next2 = [lazor_next[0] - 1, lazor_next[1] - 1]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                        lazor_path.append(lazor_next2)       

                    elif direction is [1, 1]:
                        # figure out block intercept point could be top, bot, left, right
                        if lazor_next == 'left':
                            lazor_next = [lazor_next[0] - 1, lazor_next[1] + 1]
                            lazor_next2 = [lazor_next[0] + 1, lazor_next[1] - 1]
                        elif lazor_next == 'top':
                            lazor_next = [lazor_next[0] + 1, lazor_next[1] - 1]
                            lazor_next2 = [lazor_next[0] + 1, lazor_next[1] + 1]
                        elif lazor_next == 'right' or lazor_next == 'bot':
                            lazor_next = [lazor_next[0] - 2, lazor_next[1] - 2]
                            lazor_next2 = [lazor_next[0] + 1, lazor_next[1] + 1]
                        # store all crossed blocks and lazor path
                        block_cross.append(next_block)
                        lazor_path.append(lazor_next)
                        lazor_path.append(lazor_next2)
                        
                elif next_block[1:] == 'B':
                    # opaque block, dead end
                    block_cross.append(next_block)
                    lazor_path.append(lazor_next)
                    break
            return
        pass

    
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
        return goal_left
            
    goal = goal left
        