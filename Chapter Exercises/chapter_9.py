#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:55:17 2019

@author: emilybregger
"""

import os
st = open(os.path.expanduser("~/Desktop/st.txt"), "w")
st.write("Hi from Python")
st.close()