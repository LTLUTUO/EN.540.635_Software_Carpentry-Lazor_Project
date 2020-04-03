# -*- coding: utf-8 -*-
"""
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan

"""

def put_block(x_positions, o_positions, next_block, block):
    '''
    this function puts the blocks in the grid
    
    **Parameters**
        x_positions: *list*
                      positions for "x" in grid, which mean no block can be put.
        o_positions: *list*
                      positions for "o" in grid, which mean any block can be put.
        next_block: *tuple*
                    next block position and type.
        block: *list*
                a list shows how many each types of blocks given
    '''    
    # x_positions = blocks cannot put anything
    # o_positions = open blocks

    # define next_block to be position + a random block type
    # block_type = random.choice('ABC')
    # next_block = [block_position, block_type]    
    
    if next_block[0] in x_positions:
        pass
    elif next_block[0] in o_positions:
        # 满足随机选一个block type，同时这个type试题中要求的
        if next_block[1] == 'A' and block[0] != 0:
            block = [block[0] - 1, block[1], block[2]]
        elif next_block[1] == 'B' and block[1] != 0:
            block = [block[0], block[1] - 1, block[2]]
        elif next_block[1] == 'C' and block[2] != 0:
            block = [block[0], block[1], block[2] - 1]
            
            
            

            
            