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
        
    def beam(self):
        '''
        this function calculates the slop and intersection for lazor beam
        '''
        k = (self.start[1] - self.direction[1]) / (self.start[0] - self.direction[0])
        b = self.start[1] - k * self.start[0]
        return k, b
    
    def lazor_intersect_or_nor(self, query):
        '''
        this function calculates if the query point can be intersected
        
        **Parameters**
            query: *tuple*
                   the point coordinate want to check.
                   
        '''
        self.query = query
        k, b = Lazor.beam(self)
        lazor_vector = (self.direction[0] - self.start[0], self.direction[1] - self.start[1])
        query_vector = (self.query[0] - self.start[0], self.query[1] - self.start[1])
        vector_align = lazor_vector[0] * query_vector[1] - query_vector[0] * lazor_vector[1]
        if self.query[0] * k + b == self.query[1]:
            if vector_align == 0 and query_vector[0] / lazor_vector[0] > 0:
                return True
            else:
                return False
        else:
            return False
        
    def between_two_points_or_not(self, candidate, query):
        '''
        this function checks the query point is falling between lazor start point and candidate point or not
        
        **Parameters**
            candidate: *tuple*
                       the end point of the line.
            query: *tuple*
                   the point coordinate you want to check.
                   
        '''
        self.query = query
        self.candidate = candidate
        x_cord = [self.candidate[0], self.start[0]]
        y_cord = [self.candidate[1], self.start[1]]
        if self.query[0] >= min(x_cord) and self.query[1] >= min(y_cord) and self.query[0] <= max(x_cord) and self.query[1] <= max(y_cord):
            return True
        else:
            return False
            
                
        