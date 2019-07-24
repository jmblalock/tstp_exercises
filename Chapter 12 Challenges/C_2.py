#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:44:52 2019

@author: emilybregger
"""

import math

class Circle():
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return (self.radius^2) * math.pi
    
circle = Circle(20)
print(circle.area())