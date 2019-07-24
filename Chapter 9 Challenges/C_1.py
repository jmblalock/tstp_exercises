#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:28:55 2019

@author: emilybregger
"""

import os

myList = list()

with open(os.path.expanduser("~/Desktop/fileoncomputer.txt"), "r") as f:
    myList.append(f.read())

print(myList)