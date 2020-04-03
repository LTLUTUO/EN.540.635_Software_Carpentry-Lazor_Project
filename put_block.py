# -*- coding: utf-8 -*-
"""
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan

"""


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
    grid[x][y] = block_type
    return grid
