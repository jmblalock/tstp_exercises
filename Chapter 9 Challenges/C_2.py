#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:39:00 2019

@author: emilybregger
"""

import os

with open(os.path.expanduser("~/Desktop/fileoncomputer.txt"), "w") as f:
    f.write(input("What is your favorite color? "))