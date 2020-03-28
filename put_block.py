# -*- coding: utf-8 -*-
"""
This is the Lazors Project for EN.540.635_Software_Carpentry
The code is writen by Tuo Lu and Alex Fan

"""

class Block(object):
    '''
    This class is for 3 types of blocks: reflect, opaque and refract
    '''
    def __init__(self, block_position):
        '''
        initial the block's position
        '''
        self.block_position = block_position
        
    def 