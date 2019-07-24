#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:06:53 2019

@author: emilybregger
"""

list1 = [8,19,148,4]
list2 = [9,1,33,83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)
print(list3)