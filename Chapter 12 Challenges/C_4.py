#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:55:47 2019

@author: emilybregger
"""

class Hexagon():
    def __init__(self, a):
        self.side = a
        
    def calculate_perimeter(self):
        return self.side * 6
    
hexagon = Hexagon(8)
print(hexagon.calculate_perimeter())