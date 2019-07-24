#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:21:13 2019

@author: emilybregger
"""

import re

line = "Arizona 479,501,870. California 209, 213, 650."

m = re.findall("\d",
               line,
               re.IGNORECASE)

print(m)