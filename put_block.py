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
        
    def intersect_point(self):
        '''
        this function returns possible intersection point and the intersection surface on the block.
        '''
        x_cord = 2 * self.block_position[0] + 1
        y_cord = 2 * self.block_position[1] + 1
        intersect_surface = {(x_cord, y_cord - 1): 'up', (x_cord, y_cord + 1): 'down',
                             (x_cord + 1, y_cord): 'left', (x_cord - 1, y_cord: 'right')}
        intersect_point = [(x_cord, y_cord - 1), (x_cord, y_cord + 1), (x_cord - 1, y_cord), 
                           (x_cord + 1, y_cord)]
        return intersect_point, intersect_surface
    
    def reflect(self, lazor_start, lazor_dir):
        '''
        this function calculates the reflect block
        
        **Parameters**
            lazor_start: *tuple*
                         the starting point of lazor
            lazor_dir: *tuple*
                        the direction of the lazor
        
        '''
        self.k, self.b = lazor(lazor_start, lazor_dir).line()
        self.dir = lazor_dir
        self.start = lazor_start
        intersect_point, intersect_surface = Block.intersect_point(self)
        min_distance = 'min'
        candidate = 'none'
        out_point = 'none'
        lazor_in_block = copy.deepcopy(intersect_point)
        # determine if the lazor is on block
        if self.start in lazor_in_block:
            lazor_in_block.remove(self.start)
            for i in lazor in block:
                if Lazor(self.start, self.dir).lazor_intersect_or_not(i) is True:
                    self.k = -1 / self.k
                    self.b = self.origin_point[1] - self.k * self.dir[0]
                    candidate = self.startsurface = intersect_surface.get(i)
                    if surface == 'left' or surface == 'right'
                        out_point = (self.dir[0], self.k * self.dir[0] + self.b)
                    else:
                        out_point = ((self.dir[1] - self.b) / self.k, self.dir[1])
                else:
                    pass
        else:
            for i in intersect_point:
                if Lazor(self.start, self.dir).lazor_intersect_or_not(i) is True:
                    update = np.linalg.norm(np.array(i) - np.array(self.start))
                    if update < min_distance:
                        min_distance = update
                        candidate = i
                    else:
                        continue
                else:
                    continue
            if candidate != 'none':
                self.k = -1 / self.k
                self.b = candidate[1] - self.k * candidate[0]
                surface = intersect_surface.get(candidate)
                if surface == 'left' or urface == 'right':
                    out_point = (self.start[0], self.k * self.start[0] + self.b)
                else:
                    out_point = ((self.start[1] - self.b) / self.k, self.start[1])
            else:
                out_point = 'none'
           
        return [(self.k, self.b)], candidate, out_point
            
                