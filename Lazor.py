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
    
    def return_block_cross(self, grid):
        '''
        this function lazor cross blocks or not
        
        **Parameters**
            grid: *tuple*
                   grid of the game.       
        
        '''
        self.grid = grid

        # assign lazor at starting position
        lazor = start
        block_corss = []
        while lazor in grid:
            # calculate the next point lazor will be
            next_position = [start[0] + direction[0], start[1] + direction [1]]
            next_block = block_position
            if next_block not funciton_block:
                block_cross.append(next_block)
            elif next_block is function_block:
                judge what is the block
                # change derection/slope
                    k = adsf
                # contine & change
                    contine + return new lazor (return_block_cross)
                # abosor
                    break, return
            
            
        if slope not block:
            return
        pass
    
    
    def returnpoint_cross(self):
        dict 
        pass

    
    def goal_search(self, goal):
        goal_left = []
        for i in goal:
            if i not in point_cross:
                goal_left.append(i)
        return goal_left
            
    goal = goal left
        