#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:13:37 2019

@author: emilybregger
"""

import os

myList = list()

with open(os.path.expanduser("~/Desktop/st.txt"), "r") as f:
    myList.append(f.read())

print(myList)