#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:14:44 2019

@author: emilybregger
"""

class Square():
    square_list = []
    
    def __init__(self, x):
        self.side = x
        self.square_list.append(self.side)
        
    def __repr__(self):
        return (str(self.side) + " by " 
                + str(self.side) + " by "
                + str(self.side) + " by "
                + str(self.side) + "."
                )
        
square = Square(29)
print(square)