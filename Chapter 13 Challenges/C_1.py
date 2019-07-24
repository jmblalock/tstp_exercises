#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:28:07 2019

@author: emilybregger
"""

class Shape():
    def what_am_i(self):
        print("I am a shape")
    

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def calculate_perimeter(self):
        return ((self.length*2) + (self.width*2))
    
    def change_size(self, x):
        self.length += x
        self.width += x

class Square(Rectangle):
    pass
    
a_Rectangle = Rectangle(30,10)
print(a_Rectangle.calculate_perimeter())
print(a_Rectangle.what_am_i())

a_Square = Square(4,5)
print(a_Square.calculate_perimeter())
print(a_Rectangle.what_am_i())