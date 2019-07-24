#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:50:41 2019

@author: emilybregger
"""

class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        
    def area(self):
        return (self.base * self.height) / 2
    
triangle = Triangle(10, 10)
print(triangle.area())