#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:14:44 2019

@author: emilybregger
"""

x = 0 
while x <= 35:
    x+=1
    if x <= 10:
        print("a message")
    elif x > 10 and x <= 25:
        print("another message")
    else:
        print("and another message")