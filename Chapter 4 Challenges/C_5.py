#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:00:46 2019

@author: emilybregger
"""

def f(x):
    """
    converts a string to a float and
    returns the result
    """
    try:
        y = float(x)
        return y
    except ValueError:
        print("Invalid input.")

print(f('hi'))